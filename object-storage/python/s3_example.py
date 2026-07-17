import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to Gozunga Object Storage
s3 = boto3.client(
    "s3",
    endpoint_url="https://files.fsd1.gozunga.com",
    aws_access_key_id=os.environ["GOZUNGA_S3_ACCESS_KEY"],
    aws_secret_access_key=os.environ["GOZUNGA_S3_SECRET_KEY"],
)

BUCKET = os.environ.get("GOZUNGA_S3_BUCKET", "my-bucket")

# List buckets
print("Buckets:")
for b in s3.list_buckets().get("Buckets", []):
    print(f"  {b['Name']}")

# Upload a file
s3.upload_file("s3_example.py", BUCKET, "examples/s3_example.py")
print(f"\nUploaded s3_example.py → s3://{BUCKET}/examples/s3_example.py")

# List objects in bucket
print(f"\nObjects in {BUCKET}:")
response = s3.list_objects_v2(Bucket=BUCKET)
for obj in response.get("Contents", []):
    print(f"  {obj['Key']}  ({obj['Size']} bytes)")

# Generate a presigned download URL (valid 1 hour)
url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": BUCKET, "Key": "examples/s3_example.py"},
    ExpiresIn=3600,
)
print(f"\nPresigned URL:\n  {url}")

# Download a file
s3.download_file(BUCKET, "examples/s3_example.py", "/tmp/s3_example_downloaded.py")
print("\nDownloaded → /tmp/s3_example_downloaded.py")
