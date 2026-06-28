"""
utils/permissions.py — Checks y decoradores de permisos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reutilizable por cualquier cog que necesite verificar roles/permisos.
"""

from discord.ext import commands
from utils.logger import get_logger

log = get_logger("utils.permissions")


def is_moderator():
    """Check: el usuario tiene permiso de moderación."""
    async def predicate(ctx: commands.Context):
        # Moderar mensajes es un buen indicador de moderador
        has_perm = ctx.author.guild_permissions.manage_messages
        if not has_perm:
            log.warning(f"{ctx.author} intentó usar comando de mod sin permisos")
        return has_perm
    return commands.check(predicate)


def is_admin():
    """Check: el usuario es administrador."""
    async def predicate(ctx: commands.Context):
        return ctx.author.guild_permissions.administrator
    return commands.check(predicate)
