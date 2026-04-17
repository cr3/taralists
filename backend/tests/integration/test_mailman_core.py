"""Integration tests for the mailman-core service."""

import json
import socket
import urllib.error
import urllib.request
from base64 import b64encode

from pytest_xdocker.retry import retry


def test_mailman_core_lmtp(mailman_core_service):
    """Mailman-core should accept LMTP connections on port 8024."""
    def connect():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((mailman_core_service.ip, 8024))
            return s.recv(1024).decode()

    banner = retry(connect).catching(OSError)
    assert "220" in banner


def test_mailman_core_rest_api(mailman_core_service):
    """Mailman-core REST API should respond with version info on port 8001."""
    creds = b64encode(b"restadmin:restpass").decode()

    def get_api():
        req = urllib.request.Request(
            f"http://{mailman_core_service.ip}:8001/3.1/system/versions",
            headers={"Authorization": f"Basic {creds}"},
        )
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())

    result = retry(get_api).catching(urllib.error.URLError)
    assert "api_version" in result
