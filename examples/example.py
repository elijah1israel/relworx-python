#!/usr/bin/env python
"""
Example usage of the Relworx Python SDK.

This script demonstrates basic usage of the library.
"""

import os
from relworx import RelworxClient
from relworx.exceptions import ValidationError, AuthenticationError, APIError


def main():
    # Get API key from environment variable
    api_key = os.getenv("RELWORX_API_KEY")
    
    if not api_key:
        print("Please set RELWORX_API_KEY environment variable")
        print("export RELWORX_API_KEY='your-api-key-here'")
        return

    # Initialize the client
    client = RelworxClient(api_key=api_key)

    try:
        # Example 1: Request payment from customer
        print("\n=== Requesting Payment ===")
        payment_response = client.request_payment(
            phone_number="256701234567",  # Uganda MTN number
            amount=10000,                  # 10,000 UGX
            currency="UGX",
            reference="ORDER-2024-001",
            description="Payment for Order #001",
            callback_url="https://your-website.com/webhook"
        )
        print(f"Payment Status: {payment_response.get('status')}")
        print(f"Transaction ID: {payment_response.get('transaction_id')}")
        print(f"Reference: {payment_response.get('reference')}")

        # Example 2: Send money to customer
        print("\n=== Sending Money ===")
        send_response = client.send_money(
            phone_number="256701234567",
            amount=5000,                   # 5,000 UGX
            currency="UGX",
            reference="REFUND-2024-001",
            reason="Refund for cancelled order"
        )
        print(f"Transfer Status: {send_response.get('status')}")
        print(f"Transaction ID: {send_response.get('transaction_id')}")

        # Example 3: Check transaction status
        print("\n=== Checking Transaction Status ===")
        status_response = client.get_transaction_status(reference="ORDER-2024-001")
        print(f"Transaction Status: {status_response.get('status')}")
        print(f"Amount: {status_response.get('amount')} {status_response.get('currency')}")

        # Example 4: Validate payment details
        print("\n=== Validating Payment Details ===")
        validation = client.validate_payment_details(
            phone_number="256701234567",
            currency="UGX"
        )
        print(f"Valid: {validation.get('valid')}")
        print(f"Operator: {validation.get('operator')}")

        # Example 5: Get exchange rates
        print("\n=== Getting Exchange Rates ===")
        rates = client.get_exchange_rates()
        print(f"Exchange Rates: {rates}")

    except ValidationError as e:
        print(f"\nValidation Error: {e}")
    except AuthenticationError as e:
        print(f"\nAuthentication Error: {e}")
        print("Please check your API key")
    except APIError as e:
        print(f"\nAPI Error: {e}")
        print(f"Status Code: {e.status_code}")
    finally:
        # Clean up
        client.close()


def context_manager_example():
    """Example using context manager."""
    api_key = os.getenv("RELWORX_API_KEY")
    
    if not api_key:
        print("Please set RELWORX_API_KEY environment variable")
        return

    # Using context manager (automatically closes session)
    with RelworxClient(api_key=api_key) as client:
        response = client.request_payment(
            phone_number="256701234567",
            amount=10000,
            currency="UGX",
            reference="ORDER-CTX-001"
        )
        print(f"Payment Status: {response.get('status')}")


if __name__ == "__main__":
    print("Relworx Python SDK - Example Usage")
    print("===================================")
    main()
    
    print("\n\nContext Manager Example")
    print("========================")
    context_manager_example()
