import pytest


@pytest.mark.xbox_check
def test_for_check_xbox_requirements(page_object_for_x_box):
    page_object_for_x_box.go_to()
    page_object_for_x_box.find_xbox_menu()
    page_object_for_x_box.see_more()
    page_object_for_x_box.system_requirements()
    page_object_for_x_box.join_now()
    assert page_object_for_x_box.check_title('Придбати PC Game Pass — 14-денне ознайомлення пропонується щомісяця | Xbox')