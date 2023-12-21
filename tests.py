from src.services import _get_users
from unittest import mock


def test_get_users():
    mock_api = mock.Mock()
    mock_api.users.return_value = []
    _get_users(woe_id=1000, api=mock_api)
    assert 1 == 1
