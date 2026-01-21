# Relworx Python SDK - Quick Start Guide

## Installation

```bash
pip install relworx
```

## Get Your API Key

1. Sign up: https://payments.relworx.com/users/sign_up
2. Verify your email
3. Sign in: https://payments.relworx.com/users/sign_in
4. Create a business account
5. Generate API key: https://payments.relworx.com/user/accounts/relworxhosting/api_keys/new

## Basic Usage

```python
from relworx import RelworxClient

# Initialize client
client = RelworxClient(api_key="your-api-key")

# Request payment
response = client.request_payment(
    phone_number="256701234567",  # Uganda MTN
    amount=10000,                  # 10,000 UGX
    currency="UGX",
    reference="ORDER123"
)

print(response)
```

## Test Your Installation

```python
# test_install.py
from relworx import RelworxClient
print("✓ Relworx SDK installed successfully!")
print(f"Version: {relworx.__version__}")
```

## Next Steps

1. Check out [examples/example.py](examples/example.py) for more examples
2. Read the full [README.md](README.md) for detailed documentation
3. Review [DEPLOYMENT.md](DEPLOYMENT.md) for deployment instructions

## Support

- Documentation: https://payments.relworx.com/docs/
- GitHub Issues: Report bugs and request features

## Publishing to PyPI

Ready to publish? See [DEPLOYMENT.md](DEPLOYMENT.md) for complete instructions.

Quick steps:
```bash
# 1. Update version in src/relworx/__init__.py and pyproject.toml
# 2. Update CHANGELOG.md
# 3. Build
python -m build

# 4. Check
twine check dist/*

# 5. Upload to TestPyPI (recommended first)
twine upload --repository testpypi dist/*

# 6. Upload to PyPI
twine upload dist/*
```
