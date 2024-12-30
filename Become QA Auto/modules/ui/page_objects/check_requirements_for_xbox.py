from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class XboxCheck(BasePage):
    URL = 'https://www.microsoft.com/uk-ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.set_window_size(1920, 1080)
        self.driver.get(XboxCheck.URL)
        

    def find_xbox_menu(self):
        xbox_btn = self.driver.find_element(By.ID, "shellmenu_4")
        xbox_btn.click()

    def see_more(self):
        see_more_elm = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div/div/div[1]/div/section/div/div/div/a[2]/span')
        see_more_elm.click()

    def system_requirements(self):
        sys_req_elm = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div/div[1]/div[3]/div/div/nav/ul/li[4]/a')
        sys_req_elm.click()

    def join_now(self):
        call_to_action = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div/div[1]/div[3]/div/div/nav/div[2]/button/span')
        call_to_action.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title