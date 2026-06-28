"""
utils/logger.py — Logging estructurado
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Proporciona un logger configurable con colores y niveles por módulo.
"""

import logging
import sys
from config import __init__ as config

# Forzar recarga del entorno
from dotenv import load_dotenv
load_dotenv()

import os


class ColoredFormatter(logging.Formatter):
    """Formatea logs con colores ANSI para la terminal."""

    COLORS = {
        "DEBUG": "\033[36m",     # Cyan
        "INFO": "\033[32m",      # Verde
        "WARNING": "\033[33m",   # Amarillo
        "ERROR": "\033[31m",     # Rojo
        "CRITICAL": "\033[41m",  # Fondo rojo
        "RESET": "\033[0m",
    }

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.COLORS["RESET"])
        record.levelname = f"{color}{record.levelname}{self.COLORS['RESET']}"
        return super().format(record)


def get_logger(name: str) -> logging.Logger:
    """
    Obtiene un logger configurado.
    Uso:  log = get_logger("cogs.moderacion")
          log.info("Algo pasó")
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        level = os.getenv("LOG_LEVEL", "DEBUG").upper()
        logger.setLevel(getattr(logging, level, logging.DEBUG))

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(ColoredFormatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%H:%M:%S"
        ))
        logger.addHandler(handler)

    return logger
