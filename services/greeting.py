"""
services/greeting.py — Servicio de saludos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lógica de bienvenidas, despedidas y mensajes automáticos.
Sin dependencias de Discord — puramente lógica de negocio.
"""

from utils.logger import get_logger

log = get_logger("services.greeting")


class GreetingService:
    """Gestiona la configuración y envío de saludos."""

    def __init__(self):
        self.default_greeting = "¡Bienvenido {member} al servidor {guild}!"

    def build_greeting(self, member_name: str, guild_name: str, custom_template: str = None) -> str:
        """Construye el mensaje de bienvenida interpolando variables."""
        template = custom_template or self.default_greeting
        return template.format(member=member_name, guild=guild_name)

    def build_farewell(self, member_name: str, guild_name: str) -> str:
        return f"👋 {member_name} ha abandonado {guild_name}. ¡Hasta luego!"


# Instancia singleton para compartir en toda la app
greeting_service = GreetingService()
