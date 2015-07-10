# -*- coding: utf-8 -*-
from model.group import Group

def test_add_new_group(app):
    app.group.create(Group(name="test", header="header", footer="footer"))


def test_add_empty_group(app):
    app.group.create(Group())
