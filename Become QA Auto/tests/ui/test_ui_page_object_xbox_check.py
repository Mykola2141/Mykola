import pytest


@pytest.mark.xbox_check
def test_for_check_xbox_requirements(page_object):
    page_object.go_to()
    page_object.find_xbox_menu()
    page_object.see_more()
    page_object.system_requirements()
    page_object.join_now()
    assert page_object.check_title('Придбати PC Game Pass — 14-денне ознайомлення пропонується щомісяця | Xbox')