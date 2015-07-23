# -*- coding: utf-8 -*-
from model.group import Group
import string
import random
import pytest


def random_string(prefix, max_length):
    symbols = string.ascii_letters + string.digits + string.punctuation + "" * 20
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 20)) for i
    in range(5)]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_new_group(app, group):
    old_groups = app.group.get_groups_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
