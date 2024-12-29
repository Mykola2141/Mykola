from modules.ui.page_objects.check_requirements_for_xbox import XboxCheck
import pytest


@pytest.mark.xbox_check
def test_for_check_xbox_requirements():
    xbox_sys_req = XboxCheck()
    xbox_sys_req.go_to()
    xbox_sys_req.find_xbox_menu()
    xbox_sys_req.see_more()
    xbox_sys_req.system_requirements()
    xbox_sys_req.join_now()
    xbox_sys_req.check_title('Придбати PC Game Pass — 14-денне ознайомлення пропонується щомісяця | Xbox')