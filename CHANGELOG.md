# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-01-21

### Added
- Initial release of Relworx Python SDK
- Core `RelworxClient` class for API interactions
- `request_payment()` method for payment requests
- `send_money()` method for money transfers
- `get_transaction_status()` method for transaction tracking
- `validate_payment_details()` method for pre-validation
- `get_exchange_rates()` method for currency rates
- Full exception hierarchy: `RelworxError`, `AuthenticationError`, `ValidationError`, `APIError`
- Support for all Relworx supported currencies (UGX, KES, TZS, RWF, USD)
- Context manager support for automatic resource cleanup
- Comprehensive test suite with pytest
- Type hints for better IDE support
- Detailed documentation and examples
- Support for Python 3.7+

### Features
- Easy-to-use Pythonic API
- Automatic request validation
- Detailed error messages and error handling
- Timeout configuration support
- Custom metadata support for requests
- Callback URL support for webhooks
