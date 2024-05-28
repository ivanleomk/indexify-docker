import os
import boto3
from dotenv import load_dotenv

# # Load environment variables from .env file
load_dotenv()

# Assign variables from .env
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

# Initialize a session using Amazon S3
s3 = boto3.client(
    "s3",
    region_name="ap-southeast-2",  # Sydney region
)
# Access the bucket called 'indexify-bucket'
bucket_name = "indexify-bucket"
response = s3.list_objects_v2(Bucket=bucket_name)

# Print the contents of the bucket
for obj in response.get("Contents", []):
    print(obj["Key"])
