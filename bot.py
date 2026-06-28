"""
bot.py — Fábrica del bot
━━━━━━━━━━━━━━━━━━━━━━━━
Crea y configura la instancia de commands.Bot.
Cualquier evento global (on_ready, on_message) va AQUÍ.
Los equipos NO modifican este archivo a menos que sea para añadir
eventos transversales. Los comandos van en cogs/.
"""

import discord
from discord.ext import commands
from config import PREFIX, OWNER_ID
from utils.logger import get_logger

log = get_logger("bot")


class PoppaBot(commands.Bot):
    """Subclase personalizada de Bot con eventos globales."""

    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.guilds = True

        super().__init__(
            command_prefix=PREFIX,
            intents=intents,
            owner_id=OWNER_ID or None,
            help_command=None,
        )

    async def setup_hook(self):
        """Se ejecuta ANTES de conectar. Aquí se cargan los módulos."""
        from cogs.autoloader import load_all_cogs
        await load_all_cogs(self)

    async def on_ready(self):
        log.info(f"✅ Conectado como {self.user} (ID: {self.user.id})")
        log.info(f"   Servidores: {len(self.guilds)}")
        log.info(f"   Usuarios visibles: {sum(g.member_count for g in self.guilds)}")

        # Sincronizar comandos slash (solo una vez al iniciar)
        synced = await self.tree.sync()
        log.info(f"   {len(synced)} comandos slash sincronizados")

    async def on_guild_join(self, guild: discord.Guild):
        """Bienvenida al entrar a un servidor nuevo."""
        log.info(f"📥 Entré al servidor: {guild.name} (ID: {guild.id})")

        # Sincronizar comandos en este gremio
        await self.tree.sync(guild=guild)

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)


def create_bot() -> PoppaBot:
    """Factory — única forma de instanciar el bot."""
    return PoppaBot()
