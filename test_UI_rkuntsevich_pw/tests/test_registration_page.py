import pytest
from test_UI_rkuntsevich_pw.pages.errors import registration_errors as err


@pytest.mark.smoke
def test_required_fields(registration_page):
    registration_page.open_page()
    registration_page.check_required_fields()


@pytest.mark.regression
@pytest.mark.parametrize('email', [
    'test',
    'test@mail',
    'test.com'
])
def test_email_format_error(registration_page, email):
    registration_page.open_page()
    registration_page.check_email_format_error(email)


@pytest.mark.regression
@pytest.mark.parametrize('password_data', [
    ('1234567', err.password_length_error),
    ('12345678', err.password_format_error),
    ('TestPassword', err.password_format_error),
    ('!@#$%^&*', err.password_format_error),
    ('test1234', err.password_format_error),
    ('test!@#$', err.password_format_error),
    ('TEST!@#$', err.password_format_error),
    ('TEST1234', err.password_format_error),
    ('1234!@#$', err.password_format_error)
])
def test_password_errors(registration_page, password_data):
    registration_page.open_page()
    registration_page.check_password_errors(*password_data)
