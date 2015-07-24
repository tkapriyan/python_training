# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app, json_contact):
    contact = json_contact
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
