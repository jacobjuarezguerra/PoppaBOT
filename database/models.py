"""
models.py — Modelos de datos (SQLAlchemy)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cada modelo representa una tabla. Los desarrolladores del equipo de datos
añaden nuevos modelos aquí.

Convención:
  - Un archivo = un dominio (ej: users.py, guilds.py)
  - Se importan en __all_models para que init_db los registre
"""

import datetime
from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Boolean, Text
from database.connection import Base

# Lista que el init_db recorre para crear tablas
__all_models__ = []


# ─── Ejemplo: Greetings ───
class GuildConfig(Base):
    """Configuración por servidor (saludos, auto-roles, etc.)"""
    __tablename__ = "guild_config"

    guild_id = Column(BigInteger, primary_key=True, autoincrement=False)
    prefix = Column(String(10), default="!")
    greet_channel_id = Column(BigInteger, nullable=True)
    greet_message = Column(Text, nullable=True)
    greet_enabled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


__all_models__.append(GuildConfig)


# ─── Ejemplo: User XP ───
class UserProfile(Base):
    """Perfil de usuario (niveles, XP, reputación)"""
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    guild_id = Column(BigInteger, nullable=False)
    xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    last_message_at = Column(DateTime, default=datetime.datetime.utcnow)


__all_models__.append(UserProfile)
