# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Added group"))
    old_groups = app.group.get_groups_list()
    group = Group(name="Updated name")
    group.group_id = old_groups[0].group_id
    app.group.modify_first_group(group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




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
