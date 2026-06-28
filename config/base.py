"""config/base.py — Configuración base (compartida entre dev y prod)"""

# Nombres de autores para créditos
BOT_NAME = "PoppaBot"
BOT_VERSION = "1.0.0"
AUTHOR = "Equipo PoppaBot"

# Colores por defecto para embeds
COLOR_PRIMARY = 0x5865F2   # Discord Blurple
COLOR_SUCCESS = 0x57F287
COLOR_WARNING = 0xFEE75C
COLOR_ERROR = 0xED4245

# Límites
MAX_PREFIX_COMMANDS = 50
MAX_CUSTOM_EMBED_FIELDS = 25

# Cooldowns por defecto (segundos)
DEFAULT_COOLDOWN = 3
MOD_COOLDOWN = 1
ADMIN_COOLDOWN = 0
