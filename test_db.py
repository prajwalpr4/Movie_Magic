import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import os

AWS_REGION = os.environ.get('AWS_REGION', 'ap-south-1')
dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
users_table = dynamodb.Table('MovieMagic_Users')

try:
    print("Testing DynamoDB connection...")
    response = users_table.scan(Limit=1)
    print("Success! Items:", response.get('Items', []))
except NoCredentialsError:
    print("ERROR: No AWS credentials found.")
except ClientError as e:
    print(f"ERROR: Client error: {e}")
except Exception as e:
    print(f"ERROR: {e}")
