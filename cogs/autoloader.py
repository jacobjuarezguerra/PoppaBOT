"""
autoloader.py — Carga AUTOMÁTICA de todos los cogs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cada vez que alguien crea un archivo .py en cogs/ con async def setup(bot),
se carga automáticamente. No hay que registrar nada manualmente.
"""

import os
import importlib
import pkgutil
from utils.logger import get_logger

log = get_logger("autoloader")


async def load_all_cogs(bot):
    """Recorre cogs/ e importa cada módulo (excepto __init__ y autoloader)."""
    package = __package__ or "cogs"
    package_path = os.path.dirname(__file__)

    loaded = 0
    for importer, modname, ispkg in pkgutil.iter_modules([package_path]):
        # Saltar archivos que no son cogs
        if modname.startswith("_") or modname == "autoloader":
            continue

        module = importlib.import_module(f".{modname}", package=package)

        if hasattr(module, "setup"):
            await bot.load_extension(f"{package}.{modname}")
            loaded += 1
            log.info(f"   📦 Cog cargado: {modname}")

    log.info(f"✅ {loaded} cogs cargados automáticamente")
