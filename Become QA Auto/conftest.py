import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.np_search import NPSearch
from modules.ui.page_objects.check_requirements_for_xbox import XboxCheck

class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Mykola'
        self.second_name = 'Krjuchek'

    def remove(self):
        self.name = ''
        self.second_name = ''

@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def github_commit():
    api = GitHub()
    yield api

@pytest.fixture
def github_topic():
    api = GitHub()
    yield api

@pytest.fixture
def github_emoji():
    api = GitHub()
    yield api
    
@pytest.fixture
def database():
    database = Database()
    yield database
    
@pytest.fixture
def page_object():
    page_object = NPSearch()
    yield page_object

    page_object.close()

@pytest.fixture
def page_object_for_x_box():
    page_object_for_x_box = XboxCheck()
    yield page_object_for_x_box

    page_object_for_x_box.close()
