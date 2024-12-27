from playwright.async_api import Page
from multiprocessing import context

from pytest_bdd import scenario, scenarios, given, when, then
@given('Launch the page click Login button')
def launch_Page():

    @when('I fill the valid "User Name" as "prasathv"')
    def fill_Form():

        @then('the menu bar contains the "logout" link')
        def verify_Logout():
            verify_Logout
