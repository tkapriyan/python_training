# -*- coding: utf-8 -*-
from model.group import Group

def test_add_new_group(app):
    old_groups = app.group.get_groups_list()
    group = Group(name="test", header="header", footer="footer")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# Commented out this test since it will be modified in the next task
# def test_add_empty_group(app):
#     old_groups = app.group.get_groups_list()
#     group = Group(name="")
#     app.group.create(group)
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)