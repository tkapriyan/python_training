# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_delete_random_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="Added group"))
    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.group_id)
    new_groups = db.get_groups_list()
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
