import hashlib
import os
import re
import sys
import time
import json
import urllib.request
import urllib.parse
import mimetypes

def _load_cloudinary_url():
    env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                m = re.match(r"CLOUDINARY_URL=(.+)", line.strip())
                if m:
                    os.environ.setdefault("CLOUDINARY_URL", m.group(1))
    url = os.environ.get("CLOUDINARY_URL")
    if not url:
        sys.exit("CLOUDINARY_URL not set (expected in .env or environment)")
    m = re.match(r"cloudinary://([^:]+):([^@]+)@(.+)", url)
    if not m:
        sys.exit("CLOUDINARY_URL is malformed")
    return m.group(2), m.group(1), m.group(3)  # secret, key, cloud_name

API_SECRET, API_KEY, CLOUD_NAME = _load_cloudinary_url()
SOURCE_DIR = "/Users/josh/Projects/joshberrington-site/assets/squarespace-images"
FOLDER = "joshberrington-site"

def sign(params):
    to_sign = "&".join(f"{k}={v}" for k, v in sorted(params.items()))
    return hashlib.sha1((to_sign + API_SECRET).encode()).hexdigest()

def upload_file(path):
    filename = os.path.basename(path)
    public_id = os.path.splitext(filename)[0]
    timestamp = str(int(time.time()))
    params = {
        "timestamp": timestamp,
        "folder": FOLDER,
        "public_id": public_id,
    }
    signature = sign(params)

    boundary = "----CloudinaryUploadBoundary"
    body = b""
    fields = {**params, "api_key": API_KEY, "signature": signature}
    for k, v in fields.items():
        body += f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode()

    mime_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    with open(path, "rb") as f:
        file_data = f.read()
    body += f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{filename}\"\r\nContent-Type: {mime_type}\r\n\r\n".encode()
    body += file_data
    body += f"\r\n--{boundary}--\r\n".encode()

    url = f"https://api.cloudinary.com/v1_1/{CLOUD_NAME}/image/upload"
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            return True, result.get("secure_url")
    except urllib.error.HTTPError as e:
        return False, e.read().decode()

def main():
    files = sorted(
        os.path.join(SOURCE_DIR, f)
        for f in os.listdir(SOURCE_DIR)
        if os.path.isfile(os.path.join(SOURCE_DIR, f))
    )
    print(f"Found {len(files)} files to upload")
    results = []
    failures = []
    for i, path in enumerate(files, 1):
        ok, info = upload_file(path)
        status = "OK" if ok else "FAIL"
        print(f"[{i}/{len(files)}] {status} {os.path.basename(path)}")
        if ok:
            results.append({"file": os.path.basename(path), "url": info})
        else:
            failures.append({"file": os.path.basename(path), "error": info})

    with open("/Users/josh/Projects/joshberrington-site/assets/cloudinary_manifest.json", "w") as f:
        json.dump({"uploaded": results, "failed": failures}, f, indent=2)

    print(f"\nDone. Uploaded: {len(results)}  Failed: {len(failures)}")
    if failures:
        print("Failures:")
        for fail in failures:
            print(f"  {fail['file']}: {fail['error'][:200]}")

if __name__ == "__main__":
    main()
