import pytest

@pytest.mark.ui 
def test_check_incorrect_username_page_object(page_object):
    #відкриваємо сторінку https://github.com.login
    page_object.go_to()

    #виконуємо спробу увійти в систему Github
    page_object.try_login("page_object@gmail.com", "wrong password")

    #первіряємо, що назва сторінки така,яку ми очікуємо
    assert page_object.check_title("Sign in to GitHub · GitHub")