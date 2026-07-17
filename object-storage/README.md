# Object Storage Examples

Gozunga Object Storage is S3-compatible — use any S3 SDK or tool you already know.

**Endpoint:** `https://files.fsd1.gozunga.com`

## Examples

| Language | Library | Folder |
|----------|---------|--------|
| Python | boto3 | [python/](python/) |

> More languages coming soon. PRs welcome.

## Python (boto3)

```python
import boto3

s3 = boto3.client("s3", endpoint_url="https://files.fsd1.gozunga.com")

s3.upload_file("backup.tar.gz", "my-bucket", "backup.tar.gz")
s3.download_file("my-bucket", "backup.tar.gz", "local.tar.gz")
```

**Run the full example:**

```bash
cd python
cp .env.example .env   # add your credentials
pip install -r requirements.txt
python s3_example.py
```

## Compatible tools

Works with anything that speaks S3:

- `boto3` (Python)
- `aws s3` CLI
- `s3cmd`
- `rclone`
- MinIO Client (`mc`)
- Any AWS SDK (Go, Node.js, Ruby, Java, .NET, Rust…)

## Getting credentials

Log in to [cloud.fsd1.gozunga.com](https://cloud.fsd1.gozunga.com) → **Object Storage** → **Access Keys**.
