import pytest
from utils import dicts

@pytest.fixture
def collection_fixture():
    return {"vcs": "mercurial"}


def test_get_val(collection_fixture):
    assert dicts.get_val(collection_fixture, "vcs") == "mercurial"
    assert dicts.get_val(collection_fixture, "vcs", "git") == "mercurial"
    assert dicts.get_val({}, "vcs", "git") == "git"

