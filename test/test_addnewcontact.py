# -*- coding: utf-8 -*-
from model.contact import Contact
import string
import random
import pytest


def random_string(prefix, max_length):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 20
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


# Using special pattern for phone numbers
def random_phone(prefix):
    symbols = string.digits + " " * 10 + "(" * 10 + ")" * 10 + "-" * 10
    return prefix + "".join([random.choice(symbols) for i in range(1, 21)])


# Using special pattern for emails
def random_email(prefix, max_length):
    symbols = string.ascii_letters + string.digits + "_" * 10
    username = "".join([random.choice(symbols) for i in range(random.randrange(max_length))])
    domain = "".join([random.choice(symbols) for i in range(2, 21)])
    extension = "".join([random.choice(string.ascii_letters) for i in range(3)])
    return prefix + username + "@" + domain + "." + extension


test_data = [Contact(first_name="", last_name="", address="", home_phone="",
                     work_phone="", mobile_phone="", secondary_phone="", email="",
                     email2="", email3="")] + [
                Contact(first_name=random_string("firstname", 20),
                        last_name=random_string("lastname", 20),
                        address=random_string("address", 50),
                        home_phone=random_phone("home_phone"),
                        mobile_phone=random_phone("mobile_phone"),
                        work_phone=random_phone("work_phone"),
                        secondary_phone=random_phone("secondary_phone"),
                        email=random_email("email", 30),
                        email2=random_email("email2", 30),
                        email3=random_email("email3", 30)) for i in range(5)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_new_contact(app, contact):
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
