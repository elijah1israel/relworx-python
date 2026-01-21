"""Test fixtures and configuration."""

import pytest
from unittest.mock import Mock, patch

import requests_mock


@pytest.fixture
def api_key():
    """Provide a test API key."""
    return "test-api-key-12345"


@pytest.fixture
def mock_session():
    """Provide a mock requests session."""
    with requests_mock.Mocker() as m:
        yield m


@pytest.fixture
def client():
    """Provide a RelworxClient instance."""
    from relworx import RelworxClient
    return RelworxClient(api_key="test-api-key")
