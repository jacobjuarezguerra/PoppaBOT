# PoppaBot — Discord Bot Modular
#
# Organización del proyecto para trabajo en equipo:
#
# ├── .env                  ← Secretos (token, DB, APIs) — NO se sube a git
# ├── .env.example          ← Plantilla del .env — SÍ se sube a git
# ├── main.py               ← Entry point (solo arranca)
# ├── bot.py                ← Fábrica del bot (configura intents, eventos globales)
# ├── config/
# │   ├── __init__.py       ← Carga la configuración activa
# │   ├── base.py           ← Config base compartida
# │   └── dev.py / prod.py  ← Config por entorno
# ├── database/
# │   ├── __init__.py
# │   ├── connection.py     ← Pool de conexiones (SQLite / PostgreSQL)
# │   └── models.py         ← Modelos de datos
# ├── cogs/                 ← 🟢 Cada desarrollador crea su propio archivo aquí
# │   ├── __init__.py
# │   ├── general.py        ← Comandos básicos (ping, info)
# │   ├── moderation.py     ← Moderación (kick, ban, warn)
# │   └── autoloader.py     ← Carga automática de todos los cogs
# ├── services/             ← 🟢 Lógica de negocio (sin Discord)
# │   ├── __init__.py
# │   ├── greeting.py       ← Servicio de saludos
# │   └── leveling.py       ← Servicio de niveles / XP
# ├── utils/                ← 🟢 Utilidades transversales
# │   ├── __init__.py
# │   ├── logger.py         ← Logging estructurado
# │   ├── embed.py          ← Helpers para embeds bonitos
# │   └── permissions.py    ← Decoradores de permisos
# ├── tests/                ← 🟢 Tests por módulo
# │   ├── __init__.py
# │   ├── test_services.py
# │   └── test_cogs.py
# └── assets/               ← Imágenes, JSON, etc.
