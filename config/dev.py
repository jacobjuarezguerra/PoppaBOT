"""config/dev.py — Configuraciones específicas de desarrollo"""

# Servidores donde se prueban comandos (se sincronizan más rápido que global)
DEV_GUILDS = []  # Añadir IDs: [123456789, 987654321]

# Logging más verboso
LOG_LEVEL = "DEBUG"

# Simular APIs sin llamadas reales
MOCK_EXTERNAL_API = True
