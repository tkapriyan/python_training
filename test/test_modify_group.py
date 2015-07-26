# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_random_group_name(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="Added group"))
    old_groups = db.get_groups_list()
    updated_group = Group(name="Updated name")
    group = random.choice(old_groups)
    updated_group.group_id = group.group_id
    app.group.modify_group_by_id(group.group_id, updated_group)
    # assert len(old_groups) == app.group.count()
    new_groups = db.get_groups_list()
    old_groups.remove(group)
    old_groups.append(updated_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
