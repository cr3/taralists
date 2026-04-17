"""Integration tests for the database service."""

from subprocess import CalledProcessError

import pytest
from pytest_xdocker.docker import docker
from pytest_xdocker.retry import retry

from taralists.testing.psql import psql


def test_database_version(env_vars, database_service):
    """The database service should accept connections as DBUSER."""
    query = (
        psql
        .with_host(database_service.ip)
        .with_username(env_vars["DBUSER"])
        .with_dbname(env_vars["DBNAME"])
        .with_command("SELECT VERSION();")
    )
    command = docker.exec_(database_service.name).with_env("PGPASSWORD", env_vars["DBPASS"]).with_command(*query)
    result = retry(command.execute).catching(CalledProcessError)
    assert "PostgreSQL" in result


def test_database_mailman_tables(env_vars, database_service, mailman_core_service):
    """The mailman schema should exist after mailman-core initialises."""
    query = (
        psql
        .with_host(database_service.ip)
        .with_username(env_vars["DBUSER"])
        .with_dbname(env_vars["DBNAME"])
        .with_command("SELECT tablename FROM pg_tables WHERE schemaname = 'public';")
    )
    command = docker.exec_(database_service.name).with_env("PGPASSWORD", env_vars["DBPASS"]).with_command(*query)

    def get_tables():
        result = command.execute()
        assert "mailinglist" in result
        return result

    retry(get_tables).catching((CalledProcessError, AssertionError))


def test_database_rejects_bad_credentials(env_vars, database_service):
    """The database service should reject connections with the wrong password."""
    query = (
        psql
        .with_host(database_service.ip)
        .with_username(env_vars["DBUSER"])
        .with_dbname(env_vars["DBNAME"])
        .with_command("SELECT 1;")
    )
    command = docker.exec_(database_service.name).with_env("PGPASSWORD", "wrongpassword").with_command(*query)
    with pytest.raises(CalledProcessError):
        command.execute()
