from playwright.sync_api import expect
from test_UI_rkuntsevich_pw.pages.base_page import BasePage
from test_UI_rkuntsevich_pw.pages.locators import registration_locators as loc
from test_UI_rkuntsevich_pw.pages.errors import registration_errors as err


class RegistrationPage(BasePage):
    page_path = '/customer/account/create/'

    def click_submit_btn(self):
        submit_btn = self.find(loc.submit_btn_loc)
        submit_btn.click()

    def check_required_fields(self):
        self.click_submit_btn()

        first_name_err = self.find(loc.first_name_err_loc)
        last_name_err = self.find(loc.last_name_err_loc)
        email_err = self.find(loc.email_err_loc)
        password_err = self.find(loc.password_err_loc)
        confirm_password_err = self.find(loc.password_err_confirmation_loc)

        expect(first_name_err).to_have_text(err.required_field_error)
        expect(last_name_err).to_have_text(err.required_field_error)
        expect(email_err).to_have_text(err.required_field_error)
        expect(password_err).to_have_text(err.required_field_error)
        expect(confirm_password_err).to_have_text(err.required_field_error)

    def check_email_format_error(self, text):
        email_field = self.find(loc.email_loc)
        email_field.fill(text)
        self.click_submit_btn()
        email_err = self.find(loc.email_err_loc)

        expect(email_err).to_have_text(err.email_format_error)

    def check_password_errors(self, text, error):
        password_field = self.find(loc.password_loc)
        password_field.fill(text)
        self.click_submit_btn()
        password_err = self.find(loc.password_err_loc)

        expect(password_err).to_have_text(error)
