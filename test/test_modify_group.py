# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_modify_random_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Added group"))
    old_groups = app.group.get_groups_list()
    group = Group(name="Updated name")
    index = randrange(len(old_groups))
    group.group_id = old_groups[index].group_id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# Commented out all the tests below as they will be changed in the next task anyways

# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Added group"))
#     old_groups = app.group.get_groups_list()
#     app.group.modify_first_group(Group(header="Updated header"))
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Added group"))
#     old_groups = app.group.get_groups_list()
#     app.group.modify_first_group(Group(footer="Updated footer"))
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) == len(new_groups)
