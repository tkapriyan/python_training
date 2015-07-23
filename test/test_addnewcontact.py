# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts_list = app.contact.get_contacts_list()
    contact = Contact(first_name="First", last_name="Last", address="Address", home_phone="12345678",
                      work_phone="(312)98756-32", secondary_phone="312-987-78-23", email="first.last@test.com",
                      email2="second.email@test.com")
    app.contact.create(contact)
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)

# def test_add_empty_contact(app):
#     contact = Contact(first_name="First", last_name="Last")
#     old_contacts_list = app.contact.get_contacts_list()
#     app.contact.create(contact)
#     assert len(old_contacts_list) + 1 == app.contact.count()
#     new_contacts_list = app.contact.get_contacts_list()
#     old_contacts_list.append(contact)
#     assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
