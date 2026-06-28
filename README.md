<div align="center">

# 🤖 PoppaBot

**Bot de Discord modular — diseñado para trabajar en equipo**

![Python](https://img.shields.io/badge/python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![discord.py](https://img.shields.io/badge/discord.py-2.4%2B-5865F2?style=for-the-badge&logo=discord&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0%2B-D71F00?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

---

[🚀 Comenzar](#-comenzar) • [📂 Estructura](#-estructura) • [🧠 Trabajo en equipo](#-trabajo-en-equipo) • [⚙️ Configuración](#️-configuración) • [🧪 Tests](#-tests) • [🤝 Contribuir](#-contribuir)

</div>

---

## 🚀 Comenzar

```bash
# 1. Clonar el repositorio
git clone https://github.com/jacobjuarezguerra/PoppaBOT.git
cd PoppaBOT

# 2. Crear entorno virtual e instalar dependencias
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt

# 3. Configurar el token del bot
cp .env.example .env
# Editar .env y pegar tu token de Discord en DISCORD_TOKEN=

# 4. Ejecutar
python main.py
```

> ⚠️ **Importante:** El archivo `.env` contiene el token del bot y **NO** se sube a git. Cada miembro del equipo usa su propio `.env`.

---

## 📂 Estructura

```
PoppaBot/
│
├── main.py                 # 🚀 Entry point (no tocar)
├── bot.py                  # 🔧 Fábrica del bot (no tocar)
├── .env                    # 🔑 Token y secretos (ignorado por git)
├── .env.example            # 📋 Plantilla para el .env
├── requirements.txt        # 📦 Dependencias
├── .gitignore
│
├── config/                 # ⚙️  Configuración multi-entorno
│   ├── __init__.py         #     Lee .env, detecta dev/prod
│   ├── base.py             #     Valores compartidos
│   ├── dev.py              #     Ajustes de desarrollo
│   └── prod.py             #     Ajustes de producción
│
├── cogs/                   # 🟢 COMANDOS — cada dev crea su archivo
│   ├── autoloader.py       #     Carga automática (no tocar)
│   ├── general.py          #     Ping, hola, info
│   └── moderation.py       #     Clear, kick, ban...
│
├── services/               # 🟢 LÓGICA DE NEGOCIO (sin Discord)
│   ├── greeting.py         #     Servicio de saludos
│   └── leveling.py         #     Servicio de niveles y XP
│
├── database/               # 🟢 CAPA DE DATOS
│   ├── connection.py       #     Pool SQLAlchemy async
│   └── models.py           #     Modelos (GuildConfig, UserProfile)
│
├── utils/                  # 🟢 UTILIDADES COMPARTIDAS
│   ├── logger.py           #     Logs con colores
│   ├── embed.py            #     Embeds consistentes
│   └── permissions.py      #     Decoradores de permisos
│
├── tests/                  # 🧪 TESTS (pytest, sin Discord)
│   └── test_services.py
│
└── assets/                 # 🖼️  Imágenes, JSONs, etc.
```

---

## 🧠 Trabajo en equipo

| Carpeta | Responsable | ¿Qué hace? |
|---|---|---|
| **`cogs/`** | Cada dev | Crea su propio archivo (`musica.py`, `economia.py`, `admin.py`…) y el **autoloader** lo carga automáticamente. Sin registrar nada. |
| **`services/`** | Backend | Lógica de negocio **sin importar Discord**. Se puede testear con `pytest`. |
| **`database/`** | Datos | Modelos y conexiones SQLAlchemy. |
| **`utils/`** | Infra | Helpers compartidos: logs, embeds, permisos. |
| **`config/`** | DevOps | Configuración por entorno (dev / prod). |
| **`main.py` + `bot.py`** | 🛑 Nadie toca | Estables, punto de entrada único. |

### 📌 Reglas del equipo

1. **Cada feature = un cog nuevo** — no edites cogs de otros sin hablar antes.
2. **La lógica va en `services/`** — los cogs solo reciben comandos y llaman servicios.
3. **Tests ante todo** — toda funcionalidad en `services/` debe tener su test.
4. **Nunca subas el `.env`** — usa `.env.example` como plantilla.

---

## ⚙️ Configuración

### Variables de entorno (`.env`)

| Variable | Obligatorio | Descripción |
|---|---|---|
| `DISCORD_TOKEN` | ✅ | Token del bot desde Discord Developer Portal |
| `DISCORD_PREFIX` | ❌ | Prefijo para comandos legacy (por defecto: `!`) |
| `ENVIRONMENT` | ❌ | `dev` o `prod` (por defecto: `dev`) |
| `DATABASE_URL` | ❌ | URL de conexión a BD (por defecto: SQLite local) |
| `OWNER_ID` | ❌ | ID del usuario propietario del bot |
| `GUILD_ID` | ❌ | ID del servidor para comandos rápidos en dev |

### Entornos

- **`dev`**: logs detallados, sincronización rápida de comandos (por servidor)
- **`prod`**: logs mínimos, sincronización global de comandos

---

## 🧪 Tests

Los tests unitarios de `services/` se ejecutan **sin necesidad de un bot de Discord**:

```bash
pip install -e .[dev]   # o: pip install pytest pytest-asyncio
pytest tests/ -v
```

```
tests/test_services.py ✓✓✓✓✓
```

---

## 🛠️ Añadir un comando nuevo

En **5 minutos**:

```python
# cogs/musica.py
import discord
from discord import app_commands
from discord.ext import commands


class Musica(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="play", description="Reproduce una canción")
    async def play(self, interaction: discord.Interaction, url: str):
        await interaction.response.send_message(f"🎵 Reproduciendo: {url}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Musica(bot))
```

✅ El **autoloader** lo detecta y lo carga automáticamente al iniciar el bot.

---

## 🤝 Contribuir

1. Crea una rama: `git checkout -b feature/mi-feature`
2. Haz tus cambios en tu cog / servicio
3. Escribe tests
4. Commit: `git commit -m "feat: descripción"`
5. Push: `git push origin feature/mi-feature`
6. Abre un **Pull Request** en GitHub

---

<div align="center">

Hecho con ❤️ por el **Equipo PoppaBot**

</div>
