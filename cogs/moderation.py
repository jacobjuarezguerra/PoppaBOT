"""
cogs/moderation.py — Comandos de moderación
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ejemplo de cog con permisos y checks. El equipo de moderación
trabaja en este archivo.
"""

import discord
from discord import app_commands
from discord.ext import commands
from utils.permissions import is_moderator
from utils.logger import get_logger

log = get_logger("cogs.moderation")


class Moderation(commands.Cog):
    """Comandos para moderar el servidor."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="clear", description="Elimina mensajes del canal")
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.describe(cantidad="Número de mensajes a eliminar (1-100)")
    async def clear(self, interaction: discord.Interaction, cantidad: int = 10):
        if cantidad < 1 or cantidad > 100:
            await interaction.response.send_message("❌ Usa un número entre 1 y 100", ephemeral=True)
            return

        await interaction.response.defer(ephemeral=True)
        deleted = await interaction.channel.purge(limit=cantidad)
        await interaction.followup.send(f"🧹 {len(deleted)} mensajes eliminados.", ephemeral=True)

    @app_commands.command(name="kick", description="Expulsa a un miembro")
    @app_commands.checks.has_permissions(kick_members=True)
    @app_commands.describe(miembro="Usuario a expulsar", razon="Motivo de la expulsión")
    async def kick(
        self,
        interaction: discord.Interaction,
        miembro: discord.Member,
        razon: str = "No especificada",
    ):
        if miembro.top_role >= interaction.user.top_role:
            await interaction.response.send_message("❌ No puedes expulsar a alguien con rol igual o superior", ephemeral=True)
            return

        await miembro.kick(reason=razon)
        await interaction.response.send_message(
            f"👢 **{miembro}** expulsado. Razón: {razon}", ephemerable=False
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))
    log.info("Cog 'moderation' registrado")
