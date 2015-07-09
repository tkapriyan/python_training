# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="First", last_name="Last", address="Address", home_phone="12345678", mobile_phone="987654321", email="first.last@test.com"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="", last_name="", address="", home_phone="", mobile_phone="", email=""))
    app.session.logout()
