"""Módulo Arquitetura 2099 — Padrão 2099."""

from flask import Blueprint

bp_arquitetura = Blueprint('arquitetura', __name__)

from . import arquitetura  # noqa: E402, F401