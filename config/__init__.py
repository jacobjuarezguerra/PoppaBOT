"""config/ — Sistema de configuración multi-entorno"""

import os
from dotenv import load_dotenv

# Cargar .env siempre desde la raíz del proyecto
load_dotenv()

# ─── Entorno activo ───
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")

# ─── Discord ───
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("DISCORD_PREFIX", "!")
OWNER_ID = int(os.getenv("OWNER_ID")) if os.getenv("OWNER_ID") else None
GUILD_ID = int(os.getenv("GUILD_ID")) if os.getenv("GUILD_ID") else None

# ─── Base de datos ───
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///data/poppabot.db")

# ─── Ajustes por entorno ───
if ENVIRONMENT == "prod":
    DEBUG = False
    SYNC_GLOBALLY = True   # Sincroniza comandos a nivel global
else:
    DEBUG = True
    SYNC_GLOBALLY = False  # Solo sincroniza en el servidor de pruebas
