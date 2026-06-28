"""services/ — Capa de negocio (sin dependencias de Discord)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reglas:
  - Un archivo = un servicio (dominio)
  - NO importar discord.py aquí
  - SÍ usar database/ para persistencia
  - Los cogs llaman a estos servicios

Esto permite testear la lógica sin un bot de Discord.
"""
