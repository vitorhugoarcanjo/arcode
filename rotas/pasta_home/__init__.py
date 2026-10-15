"""Módulo Home — Padrão 2099."""

from flask import Blueprint

bp_home = Blueprint('home', __name__)

from . import home  # noqa: E402, F401