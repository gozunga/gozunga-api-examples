import openstack
from dotenv import load_dotenv
import os
import sys

load_dotenv()
openstack.enable_logging(os.getenv('GOZUNGA_DEBUG', False), stream=sys.stdout)

conn = openstack.connect(
    auth_url=os.getenv('GOZUNGA_AUTH_URL', 'https://cloud.fsd1.gozunga.com:5000/v3'),
    auth_type=os.getenv('GOZUNGA_AUTH_TYPE', 'v3applicationcredential'),
    region_name=os.getenv('GOZUNGA_REGION_NAME', 'SiouxFalls'),
    application_credential_id=os.getenv('GOZUNGA_CREDENTIAL_ID'),
    application_credential_secret=os.getenv('GOZUNGA_CREDENTIAL_SECRET'),
    app_name='gozunga-python-example',
    app_version='0.0.1'
)


# Get current authenticated user info
current_user_id = conn.current_user_id
current_project_id = conn.current_project_id

user = conn.get_user_by_id(current_user_id)
print(f"user id = {current_user_id}")
print(f"email = {user.email}")
print(f"project id = {current_project_id}")

for server in conn.compute.servers():
    print(f"id = {server.id}")
    print(f"name = {server.name}")
    print(f"status = {server.status}")
    print(f"ip = {server.addresses['Internet'][0]['addr']}")

