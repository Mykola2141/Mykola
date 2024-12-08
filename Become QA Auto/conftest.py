import pytest
from modules.api.clients.github import GitHub

class User:
    def __init__(self) ->None:
        self.name=None
        self.second_name=None

    def create(self):
        self.name='Mykola'
        self.second_name='Krjuchek'

    def remove(self):
        self.name=''
        self.second_name=''

@pytest.fixture
def user():
    user=User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api=GitHub()
    yield api


@pytest.fixture
def github_commit():
    commit1=GitHub()
    yield commit1

@pytest.fixture
def github_topic():
    topic1=GitHub()
    yield topic1