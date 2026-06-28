<div align="center">

# 🤖 PoppaBot

**Bot de Discord con bienvenidas y despedidas automáticas**

![Node.js](https://img.shields.io/badge/node.js-18%2B-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![discord.js](https://img.shields.io/badge/discord.js-14%2B-5865F2?style=for-the-badge&logo=discord&logoColor=white)
![Render](https://img.shields.io/badge/deploy-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

---

[🚀 Comenzar](#-comenzar) • [⚙️ Configuración](#️-configuración) • [📁 Estructura](#-estructura) • [🌐 Despliegue](#-despliegue-en-render)

</div>

---

## 🚀 Comenzar

```bash
# 1. Clonar
git clone https://github.com/jacobjuarezguerra/PoppaBOT.git
cd PoppaBOT

# 2. Instalar dependencias
npm install

# 3. Configurar
cp .env.example .env
# Editar .env con tu token de Discord

# 4. Iniciar
npm start
```

---

## ⚙️ Configuración

Editar el archivo `.env`:

```env
DISCORD_TOKEN=pon_aqui_tu_token    # Token del bot (Discord Developer Portal)
WELCOME_CHANNEL=bienvenida         # Nombre del canal de bienvenidas
GOODBYE_CHANNEL=despedidas         # Nombre del canal de despedidas
```

### Canales requeridos

El bot busca canales por **nombre** en tu servidor:

| Canal | Propósito |
|---|---|
| `#bienvenida` | Mensaje embed cuando alguien entra |
| `#despedidas` | Mensaje embed cuando alguien se va |

> Puedes cambiar los nombres en el `.env`.

---

## 📁 Estructura

```
PoppaBot/
├── src/
│   └── index.js           # 🚀 Código principal del bot
├── package.json           # 📦 Dependencias y scripts
├── .env                   # 🔑 Token y configuración (no se sube a git)
├── .env.example           # 📋 Plantilla del .env
└── .gitignore
```

---

## 🤖 Funcionalidades

### ✅ Bienvenidas
Cuando un usuario entra al servidor, el bot envía un embed con:
- Avatar del usuario
- Nombre y mención
- Fecha de creación de la cuenta
- Conteo actual de miembros

### 👋 Despedidas
Cuando un usuario sale, el bot envía un embed con:
- Avatar del usuario
- Tag del usuario
- Miembros restantes

### 💚 Health Check
Incluye un servidor HTTP en el puerto `3000` (o `PORT` variable) para que plataformas como **Render** verifiquen que el bot está activo.

---

## 🌐 Despliegue en Render

Este bot está listo para desplegarse en [Render](https://render.com):

1. Crea un **Web Service**
2. Conecta tu repositorio de GitHub
3. Configura:
   - **Build Command:** `npm install`
   - **Start Command:** `npm start`
4. Añade las variables de entorno en Render (las del `.env`)
5. ¡Listo! 🚀

El health check HTTP en `puerto 10000` (Render asigna `PORT` automáticamente) mantiene el servicio activo.

---

## 📦 Dependencias

- [discord.js v14](https://discord.js.org/) — API de Discord
- [dotenv](https://github.com/motdotla/dotenv) — Variables de entorno
- [Node.js](https://nodejs.org/) — Entorno de ejecución

---

<div align="center">

Hecho con ❤️ por **jacobjuarezguerra**

</div>
