# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Added contact"))
    old_contacts_list = app.contact.get_contacts_list()
    index = randrange(len(old_contacts_list))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts_list) - 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    old_contacts_list[index:index + 1] = []
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
