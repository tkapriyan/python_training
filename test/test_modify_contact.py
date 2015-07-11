# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Added contact"))
    app.contact.modify_first_contact(Contact(first_name="New_name", last_name="New_Last_name", address="New_Address", home_phone="11111111", mobile_phone="111111111", email="new.first.last@test.com"))

def test_modify_first_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Added contact"))
    app.contact.modify_first_contact(Contact(address="New_Address"))

def test_modify_first_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Added contact"))
    app.contact.modify_first_contact(Contact(last_name="New_Last_name"))

def test_modify_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Added contact"))
    app.contact.modify_first_contact(Contact(email="new.emailaddress@test.com"))


