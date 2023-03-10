import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[contains(@class, 'MuiButtonBase-root MuiButton-root')]"
    scouts_panel_title_xpath = "//*[contains(@class, 'MuiTypography-root MuiTypography-h5')]"
    remind_password_xpath = "//*[contains(@class, 'MuiTypography-root MuiLink')]"
    select_language_xpath = "//*[contains(@class, 'MuiSelect-root MuiSelect')]"
    password_invalid_message_xpath = "//*[@id='__next']/form/div/div[1]/div[3]/span"

    # Login URL and expected title for test
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    expected_title = "Scouts panel - sign in"
    header_of_box = 'Scouts Panel'
    expected_invalid_password = "Identifier or password invalid."

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def check_login_page_title(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_scout_panel_text_label(self):
        self.assert_element_text(self.driver, self.scouts_panel_title_xpath, self.header_of_box)

    def check_invalid_password_message(self):
        self.visibility_of_element_located(self.password_invalid_message_xpath, self.expected_invalid_password)

    def create_screen_shoot_login_page(self, save_name):
        self.screen_shoot(save_name)


