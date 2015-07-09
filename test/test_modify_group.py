# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="updated", header="new_header", footer="new_footer"))
    app.session.logout()