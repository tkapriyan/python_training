# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Added contact"))
    old_contacts_list = app.contact.get_contacts_list()
    modified_contact = Contact(first_name="New_name", last_name="New_Last_name", address="New_Address",
                               home_phone="11111111", mobile_phone="111111111", email="new.first.last@test.com")
    modified_contact.contact_id = old_contacts_list[0].contact_id
    app.contact.modify_first_contact(modified_contact)
    assert len(old_contacts_list) == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    old_contacts_list[0] = modified_contact
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)

# Commented out all the tests below as they will be changed in the next task anyways


# def test_modify_first_contact_address(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="Added contact"))
#     app.contact.modify_first_contact(Contact(address="New_Address"))
#
# def test_modify_first_contact_last_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="Added contact"))
#     app.contact.modify_first_contact(Contact(last_name="New_Last_name"))
#
# def test_modify_first_contact_email(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="Added contact"))
#     app.contact.modify_first_contact(Contact(email="new.emailaddress@test.com"))
