"""
utils/embed.py — Helpers para crear embeds consistentes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Unifica el estilo visual de todos los mensajes del bot.
"""

import discord
from config.base import COLOR_PRIMARY, COLOR_SUCCESS, COLOR_WARNING, COLOR_ERROR, BOT_NAME


def create_embed(
    title: str = None,
    description: str = None,
    color: str = "primary",
    fields: list = None,
    footer: str = None,
    author: str = None,
) -> discord.Embed:
    """
    Crea un embed con el estilo del bot.

    Args:
        color: "primary" | "success" | "warning" | "error" | int
        fields: [(name, value, inline), ...]
    """
    color_map = {
        "primary": COLOR_PRIMARY,
        "success": COLOR_SUCCESS,
        "warning": COLOR_WARNING,
        "error": COLOR_ERROR,
    }

    embed_color = color_map.get(color, COLOR_PRIMARY) if isinstance(color, str) else color

    embed = discord.Embed(
        title=title,
        description=description,
        color=embed_color,
    )

    if fields:
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

    embed.set_footer(text=footer or BOT_NAME)

    return embed


def error_embed(description: str) -> discord.Embed:
    """Atajo para mensajes de error."""
    return create_embed(description=description, color="error")


def success_embed(description: str) -> discord.Embed:
    """Atajo para mensajes de éxito."""
    return create_embed(description=description, color="success")
