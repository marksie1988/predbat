from __future__ import annotations

import os
import subprocess

import nox
from nox.sessions import Session


@nox.session(reuse_venv=True)
def format(session: Session) -> None:
    """Run automatic code formatters"""
    session.run("poetry", "install", external=True)
    session.run("black", ".")
    session.run("isort", ".")
    session.run("autoflake", "--in-place", ".")
