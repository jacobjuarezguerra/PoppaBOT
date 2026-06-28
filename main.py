# PoppaBot — Entry Point
#
# Los desarrolladores NO tocan este archivo.
# Solo ejecuta:  python main.py

import os
import sys

# Asegura que el directorio raíz esté en el path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bot import create_bot
from config import ENVIRONMENT, TOKEN, PREFIX


if __name__ == "__main__":
    if not TOKEN or TOKEN == "pon_aqui_tu_token":
        print("❌ ERROR: No has configurado el token del bot.")
        print("   → Abre el archivo .env y pega tu token en DISCORD_TOKEN")
        print("   → .env.example tiene la plantilla (cópialo si falta)")
        sys.exit(1)

    print(f"🚀 Iniciando PoppaBot — Entorno: {ENVIRONMENT}")
    bot = create_bot()
    bot.run(TOKEN)
