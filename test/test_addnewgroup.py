# -*- coding: utf-8 -*-
from model.group import Group

def test_add_new_group(app):
    old_groups = app.group.get_groups_list()
    app.group.create(Group(name="test", header="header", footer="footer"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_groups_list()
    app.group.create(Group())
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)
