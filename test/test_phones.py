# -*- coding: utf-8 -*-
import re


def test_home_page_phones(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.home_phone == clear(contact_from_edit_page.home_phone)
    assert contact_from_home_page.work_phone == clear(contact_from_edit_page.work_phone)
    assert contact_from_home_page.mobile_phone == clear(contact_from_edit_page.mobile_phone)
    assert contact_from_home_page.secondary_phone == clear(contact_from_edit_page.secondary_phone)


def clear(s):
    return re.sub("[() -]", "", s)
