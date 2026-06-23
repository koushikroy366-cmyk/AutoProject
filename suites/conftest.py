import os
import sys
import pytest
import base64
import warnings
import urllib3
import allure
from data.Variables import *
from playwright.sync_api import Page


# Ensure project root is on sys.path so imports like `data.Variables` work
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="http://localhost",
        help="Base URL for tests",
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")

