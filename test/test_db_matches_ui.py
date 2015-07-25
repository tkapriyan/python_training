from model.group import Group


def test_groups_list(app, db):
    ui_list = app.group.get_groups_list()

    def clean(group):
        return Group(group_id=group.group_id, name=group.name.strip())

    db_list = map(clean, db.get_groups_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
