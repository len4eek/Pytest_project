from Pages.LoginPage import LogIn


def test_autorization(browser):

    user_login = LogIn(browser)
    user_login.go_to_site()
    user_login.login_form()
    user_login.submit_login("0991239848", "Qwerty333")

    assert user_login.profile_name().text == "Name\nLastName"

