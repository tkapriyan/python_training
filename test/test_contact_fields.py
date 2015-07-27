# -*- coding: utf-8 -*-
import re
from fixture.contact import Contact


def test_home_page_fields(app, db):
    home_page_contacts_list = map(format_entry, app.contact.get_contacts_list())
    # home_page_contacts_list = map(format_entry, app.contact.get_contacts_list())
    db_contacts_list = map(format_entry, db.get_contacts_list())
    # db_contacts_list = map(format_entry, db.get_contacts_list())
    assert sorted(home_page_contacts_list, key=Contact.id_or_max) == sorted(db_contacts_list, key=Contact.id_or_max)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

def format_entry(contact):
        return Contact(contact_id=contact.contact_id, first_name=contact.first_name.strip(),
                       last_name=contact.last_name.strip(),
                       all_phones_from_home_page=merge_phones_like_on_home_page(contact),
                       all_emails_from_home_page=merge_emails_like_on_home_page(contact))
