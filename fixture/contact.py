class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        # Initiate contact creation
        self.open_contacts_page()
        self.fill_contact_form(contact)
        # Submit form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # Return to home page
        self.return_to_home_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        # Initiate contact modification
        wd.find_element_by_xpath(" //*[@id='maintable']//tr[5]/td[8]/a").click()
        self.fill_contact_form(contact)
        # Submit modifications
        wd.find_element_by_name("update").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("address", contact.first_name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        # Initiate contact deletion
        wd.find_element_by_name("selected[]").click()
        # Submit contact deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
