"""
cogs/general.py — Comandos generales
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cualquier desarrollador puede editar este archivo o crear nuevos cogs.
"""

import discord
from discord import app_commands
from discord.ext import commands
from utils.embed import create_embed
from utils.logger import get_logger

log = get_logger("cogs.general")


class General(commands.Cog):
    """Comandos básicos de utilidad."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Latencia del bot")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        embed = create_embed(
            title="🏓 Pong!",
            description=f"Latencia: **{latency}ms**",
            color="primary",
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="hola", description="El bot te saluda")
    async def hola(self, interaction: discord.Interaction):
        embed = create_embed(
            description=f"👋 ¡Hola {interaction.user.mention}! Soy **{self.bot.user.name}**",
            color="success",
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="info", description="Información del bot")
    async def info(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🤖 PoppaBot",
            description="Bot modular de código abierto",
            color=discord.Color.blurple(),
        )
        embed.add_field(name="Versión", value="1.0.0", inline=True)
        embed.add_field(name="Desarrollado por", value="Equipo PoppaBot", inline=True)
        embed.add_field(name="Servidores", value=str(len(self.bot.guilds)), inline=True)
        embed.add_field(name="Comandos", value=f"{len(self.bot.tree.get_commands())}", inline=True)

        await interaction.response.send_message(embed=embed)

    # ─── Comando con prefijo (legacy) ───
    @commands.command(name="ping")
    async def ping_prefix(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"🏓 Pong! {latency}ms")


async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))
    log.info("Cog 'general' registrado")
