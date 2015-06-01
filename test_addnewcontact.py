# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_new_contact(Contact(first_name="First", last_name="Last", address="Address", home_phone="12345678", mobile_phone="987654321", email="first.last@test.com"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_new_contact(Contact(first_name="", last_name="", address="", home_phone="", mobile_phone="", email=""))
    app.session.logout()
