# -*- coding: utf-8 -*-
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    contacts_cache = None

    def open_contacts_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_xpath("//table[@id='maintable']//a[.='Last name']")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_add_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_form()
        self.fill_contact_form(contact)
        # Submit form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # Return to home page
        self.return_to_home_page()
        self.contacts_cache = None

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_edit_form_by_index(index)
        self.fill_contact_form(contact)
        # Submit modifications
        wd.find_element_by_name("update").click()
        self.contacts_cache = None

    def open_contact_edit_form_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        # Initiate contact modification
        wd.find_elements_by_css_selector("img[alt=\"Edit\"]")[index].click()

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("phone2", contact.secondary_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("address", contact.address)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        # Initiate contact deletion
        wd.find_elements_by_name("selected[]")[index].click()
        # Submit contact deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                last_name = cells[1].text
                first_name = cells[2].text
                contact_id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contacts_cache.append(
                    Contact(contact_id=contact_id, first_name=first_name, last_name=last_name, home_phone=all_phones[0],
                            mobile_phone=all_phones[1], work_phone=all_phones[2], secondary_phone=all_phones[3]))
        return list(self.contacts_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_form_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        contact_id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, contact_id=contact_id, home_phone=home_phone,
                       mobile_phone=mobile_phone, work_phone=work_phone, secondary_phone=secondary_phone)
