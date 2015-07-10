# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="Updated name"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="Updated header"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="Updated footer"))
