import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user=github_api.get_user('defunkt')
    assert user['login']=='defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r=github_api.get_user('butenkosergii')
    assert r['message']== 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r=github_api.search_repo('become-qa-auto')
    assert r['total_count']==58
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r=github_api.search_repo('sergij_butenko_repo_non_exist')
    assert r['total_count']==0



@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r=github_api.search_repo('s')
    assert r['total_count'] !=0

@pytest.mark.commit
def test_commit_exist(github_commit):
    commit=github_commit.get_commit('Spoon Knife css')
    assert commit['total_count']==28

@pytest.mark.commit
def test_commit_not_exist(github_commit):
    r=github_commit.get_commit('this commit not exist and it is true474512')
    assert r['total_count']==0

@pytest.mark.topic
def test_topic_exist(github_topic):
    r=github_topic.get_topic('QA')
    assert r['total_count']==386

    
@pytest.mark.topic
def test_topic_not_exist(github_topic):
    r=github_topic.get_topic('this topic not exist')
    assert r['total_count']==0
