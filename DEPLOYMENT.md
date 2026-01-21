# Relworx Python SDK - Deployment Guide

## Preparing for PyPI Deployment

### 1. Update Package Information

Edit `pyproject.toml` and `setup.py` with your information:
- `author` and `author_email`
- Repository URL
- Package description

### 2. Create PyPI Account

1. Go to [PyPI](https://pypi.org) and create an account
2. Enable two-factor authentication for security
3. Create an API token in your account settings

### 3. Local Testing

```bash
# Install build tools
pip install build twine pytest pytest-cov

# Run tests
pytest

# Build distribution
python -m build

# Check distribution
twine check dist/*

# Test upload (optional but recommended)
twine upload --repository testpypi dist/*
```

### 4. Build Distribution

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build wheel and source distribution
python -m build

# Verify builds
ls -lh dist/
```

### 5. Upload to PyPI

```bash
# Using API token
twine upload dist/* --skip-existing

# Or with stored credentials
twine upload dist/*
```

### 6. Verify Installation

```bash
pip install relworx
python -c "import relworx; print(relworx.__version__)"
```

## Version Management

When releasing a new version:

1. Update version in `src/relworx/__init__.py`
2. Update version in `pyproject.toml`
3. Update `CHANGELOG.md`
4. Commit and tag: `git tag v0.1.0`
5. Push and build: `python -m build`
6. Upload: `twine upload dist/*`

## GitHub Actions (Optional)

Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install build twine
      - run: python -m build
      - run: twine upload dist/*
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
```

Then add `PYPI_API_TOKEN` to your repository secrets.

## Troubleshooting

### Invalid Distribution
```bash
# Check for issues
twine check dist/*

# Common fixes:
# - Update README format
# - Fix classifier names
# - Ensure version is valid semantic version
```

### Upload Fails
```bash
# Verify credentials
twine upload --skip-existing dist/*

# Check for duplicate version
pip search relworx
```

## Support

For issues, visit: https://github.com/yourusername/relworx-python/issues
