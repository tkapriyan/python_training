# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_random_contact(app):
    if app.contact.count() == 0:
        contact = Contact(first_name="First", last_name="Last", address="Address", home_phone="12345678",
                          mobile_phone="987654321", work_phone="(312)98756-32", secondary_phone="312-987-78-23",
                          email="first.last@test.com", email2="second.email@test.com", email3="third@test.com")
        app.contact.create(contact)
    old_contacts_list = app.contact.get_contacts_list()
    modified_contact = Contact(first_name="New_name", last_name="New_Last_name", address="New_Address",
                               home_phone="11111111", mobile_phone="111111111", email="new.first.last@test.com")
    index = randrange(len(old_contacts_list))
    modified_contact.contact_id = old_contacts_list[index].contact_id
    app.contact.modify_contact_by_index(index, modified_contact)
    assert len(old_contacts_list) == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    old_contacts_list[index] = modified_contact
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list,
                                                                      key=Contact.id_or_max)

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
