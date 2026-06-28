"""
connection.py — Pool de conexiones a base de datos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Soporta SQLite (dev) y PostgreSQL (prod) mediante SQLAlchemy async.
"""

import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import DATABASE_URL
from utils.logger import get_logger

log = get_logger("database")

# ─── Motor asíncrono ───
engine = create_async_engine(DATABASE_URL, echo=False)

# ─── Fábrica de sesiones ───
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    """Clase base para modelos declarativos."""
    pass


async def init_db():
    """Crear todas las tablas. Llamar en setup_hook del bot."""
    from database.models import __all_models  # noqa: import obliga a registrar modelos

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    log.info("📦 Base de datos inicializada")


async def get_session() -> AsyncSession:
    """Obtener una sesión de base de datos (context manager)."""
    async with AsyncSessionLocal() as session:
        yield session


async def close_db():
    """Cerrar conexiones. Llamar al apagar el bot."""
    await engine.dispose()
    log.info("📦 Conexiones de base de datos cerradas")
