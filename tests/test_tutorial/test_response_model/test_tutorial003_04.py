import pytest
from readyapi.exceptions import ReadyApiError


def test_invalid_response_model():
    with pytest.raises(ReadyApiError):
        from docs_src.response_model.tutorial003_04 import app

        assert app  # pragma: no cover