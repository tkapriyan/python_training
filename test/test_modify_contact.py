# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_random_contact(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="First", last_name="Last", address="Address", home_phone="12345678",
                                   work_phone="(312)98756-32", secondary_phone="312-987-78-23",
                                   email="first.last@test.com", email2="second.email@test.com"))
    old_contacts_list = db.get_contacts_list()
    modified_contact = Contact(first_name="New_name", last_name="New_Last_name", address="New_Address",
                               home_phone="11111111", mobile_phone="111111111", email="new.first.last@test.com")
    contact = random.choice(old_contacts_list)
    modified_contact.contact_id = contact.contact_id
    app.contact.modify_contact_by_id(modified_contact.contact_id, modified_contact)
    new_contacts_list = db.get_contacts_list()
    old_contacts_list.remove(contact)
    old_contacts_list.append(modified_contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list,
                                                                      key=Contact.id_or_max)
