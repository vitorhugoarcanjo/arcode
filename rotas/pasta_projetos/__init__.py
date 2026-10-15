"""Módulo Projetos — Padrão 2099."""

from flask import Blueprint

bp_projetos = Blueprint('projetos', __name__)

from . import projetos  # noqa: E402, F401