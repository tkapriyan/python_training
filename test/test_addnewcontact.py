# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.contact.create(Contact(first_name="First", last_name="Last", address="Address", home_phone="12345678", mobile_phone="987654321", email="first.last@test.com"))


def test_add_empty_contact(app):
    app.contact.create(Contact())
