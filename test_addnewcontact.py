# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(first_name="First", last_name="Last", address="Address", home_phone="12345678", mobile_phone="987654321", email="first.last@test.com"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(first_name="", last_name="", address="", home_phone="", mobile_phone="", email=""))
    app.logout()
