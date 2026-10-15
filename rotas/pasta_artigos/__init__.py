# rotas\pasta_artigos\__init__.py
"""Módulo Artigos — Padrão 2099."""

from flask import Blueprint

bp_artigos = Blueprint('artigos', __name__)

from . import artigos  # noqa: E402, F401