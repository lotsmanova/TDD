import pytest
from utils import dicts

@pytest.fixture
def collection_fixture():
    return {"vcs": "mercurial", "key": "value"}


def test_get_val(collection_fixture):
    assert dicts.get_val(collection_fixture, "key") == "value"
    assert dicts.get_val(collection_fixture, "vcs", "git") == "mercurial"
    assert dicts.get_val({}, "vcs", "git") == "git"
