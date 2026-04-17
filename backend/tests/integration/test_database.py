"""Integration tests for the database service."""

from subprocess import CalledProcessError

import pytest
from pytest_xdocker.docker import docker
from pytest_xdocker.retry import retry


def test_database_version(env_vars, database_service):
    """The database service should accept connections as DBUSER."""
    command = (
        docker.exec_(database_service.name)
        .with_env("PGPASSWORD", env_vars["DBPASS"])
        .with_command(
            "psql",
            f"--username={env_vars['DBUSER']}",
            f"--dbname={env_vars['DBNAME']}",
            "--command=SELECT VERSION();",
        )
    )
    result = retry(command.execute).catching(CalledProcessError)
    assert "PostgreSQL" in result


def test_database_rejects_bad_credentials(env_vars, database_service):
    """The database service should reject connections with the wrong password."""
    command = (
        docker.exec_(database_service.name)
        .with_env("PGPASSWORD", "wrongpassword")
        .with_command(
            "psql",
            f"--username={env_vars['DBUSER']}",
            f"--dbname={env_vars['DBNAME']}",
            "--command=SELECT 1;",
        )
    )
    with pytest.raises(CalledProcessError):
        command.execute()
