"""Psql command module."""

from pytest_xdocker.command import Command, OptionalArg, arg_type


class PsqlCommand(Command):
    """Builds a psql command declaratively."""

    with_dbname = OptionalArg("--dbname", arg_type, converter=str)
    with_host = OptionalArg("--host", arg_type, converter=str)
    with_username = OptionalArg("--username", arg_type, converter=str)
    with_command = OptionalArg("--command", arg_type, converter=str)
    with_no_password = OptionalArg("--no-password")


psql = PsqlCommand("psql")
