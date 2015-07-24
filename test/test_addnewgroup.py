# -*- coding: utf-8 -*-
from model.group import Group
from data.group import constant as test_data
import pytest


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_new_group(app, group):
    old_groups = app.group.get_groups_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
