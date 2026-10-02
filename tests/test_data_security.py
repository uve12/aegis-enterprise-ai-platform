from agents.aegis.data_analyst.tools import validate_read_only_sql


TABLE = "demo-project.aegis_demo.orders"


def test_select_is_allowed():
    ok, reason = validate_read_only_sql(
        "SELECT category FROM `demo-project.aegis_demo.orders`",
        TABLE,
    )
    assert ok is True
    assert reason == "OK"


def test_drop_is_rejected():
    ok, _ = validate_read_only_sql(
        "DROP TABLE `demo-project.aegis_demo.orders`",
        TABLE,
    )
    assert ok is False


def test_delete_is_rejected():
    ok, _ = validate_read_only_sql(
        "DELETE FROM `demo-project.aegis_demo.orders` WHERE TRUE",
        TABLE,
    )
    assert ok is False


def test_other_table_is_rejected():
    ok, _ = validate_read_only_sql(
        "SELECT * FROM `demo-project.secret_data.users`",
        TABLE,
    )
    assert ok is False
