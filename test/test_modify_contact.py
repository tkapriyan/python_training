# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(first_name="New_name", last_name="New_Last_name", address="New_Address", home_phone="11111111", mobile_phone="111111111", email="new.first.last@test.com"))
