
def test_login(app, soap):
    assert app.session.is_logged_in_as("administrator")
    soap.can_login()
