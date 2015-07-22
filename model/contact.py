# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:
    def __init__(self, first_name=None, last_name=None, address=None, home_phone=None, mobile_phone=None,
                 work_phone=None, secondary_phone=None, email=None, email2=None, email3=None, contact_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.contact_id = contact_id

    def __repr__(self):
        return "%s:%s:%s" % (self.contact_id, self.rst_name, self.last_name)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id) \
               and self.first_name == other.first_name \
               and self.last_name == other.last_name

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
