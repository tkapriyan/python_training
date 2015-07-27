# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import time


def test_delete_random_contact(app, db):
    if app.contact.count() == 0:
          contact = Contact(first_name="First", last_name="Last", address="Address", home_phone="12345678",
                      mobile_phone="987654321", work_phone="(312)98756-32", secondary_phone="312-987-78-23", email="first.last@test.com", email2="second.email@test.com", email3="third@test.com")
          app.contact.create(contact)
    old_contacts_list = db.get_contacts_list()
    contact_to_delete = random.choice(old_contacts_list)
    app.contact.delete_contact_by_id(contact_to_delete.contact_id)
    time.sleep(2)
    new_contacts_list = db.get_contacts_list()
    old_contacts_list.remove(contact_to_delete)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
