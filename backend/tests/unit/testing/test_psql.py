"""Unit tests for the psql command."""

from taralists.testing.psql import psql


def test_psql_default():
    assert psql == ["psql"]


def test_psql_with_host():
    assert psql.with_host("127.0.0.1") == ["psql", "--host", "127.0.0.1"]


def test_psql_with_username():
    assert psql.with_username("alice") == ["psql", "--username", "alice"]


def test_psql_with_dbname():
    assert psql.with_dbname("mydb") == ["psql", "--dbname", "mydb"]


def test_psql_with_command():
    assert psql.with_command("SELECT 1;") == ["psql", "--command", "SELECT 1;"]


def test_psql_with_no_password():
    assert psql.with_no_password() == ["psql", "--no-password"]


def test_psql_chained():
    command = (
        psql
        .with_host("10.0.0.1")
        .with_username("bob")
        .with_dbname("prod")
        .with_command("SELECT VERSION();")
    )
    assert command == ["psql", "--host", "10.0.0.1", "--username", "bob", "--dbname", "prod", "--command", "SELECT VERSION();"]
