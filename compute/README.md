# Compute Examples

Manage Gozunga virtual servers using the OpenStack SDK.

## Examples

| Language | Library | Folder |
|----------|---------|--------|
| Python | openstacksdk | [python/](python/) |

## Python (openstacksdk)

```bash
cd python
cp .env.example .env   # add your application credentials
pip install -r requirements.txt
python example.py
```

The example lists your running servers and prints basic info (ID, name, status, IP).

## Getting credentials

Log in to [cloud.fsd1.gozunga.com](https://cloud.fsd1.gozunga.com) → **Identity** → **Application Credentials** → **Create**.
