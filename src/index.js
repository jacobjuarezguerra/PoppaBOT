const { Client, GatewayIntentBits } = require('discord.js');
const http = require('http');
require('dotenv').config();

const PORT = process.env.PORT || 3000;
http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('PoppaBot online');
}).listen(PORT, () => console.log(`Servidor HTTP en puerto ${PORT}`));

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMembers,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
  ],
});

client.once('clientReady', () => {
  console.log(`✅ Bot conectado como ${client.user.tag}`);
});

client.on('guildMemberAdd', async (member) => {
  const channelName = process.env.WELCOME_CHANNEL || 'bienvenida';
  const channel = member.guild.channels.cache.find(
    (ch) => ch.name === channelName
  );
  if (!channel) return;

  await channel.send({
    embeds: [
      {
        color: 0x00ff00,
        title: '¡Bienvenido!',
        description: `Bienvenido al servidor, ${member.user}. ¡Esperamos que disfrutes tu estancia!`,
        thumbnail: {
          url: member.user.displayAvatarURL({ dynamic: true, size: 512 }),
        },
        fields: [
          {
            name: 'Miembros',
            value: `${member.guild.memberCount}`,
            inline: true,
          },
          {
            name: 'Cuenta creada',
            value: `<t:${Math.floor(member.user.createdTimestamp / 1000)}:R>`,
            inline: true,
          },
        ],
        footer: {
          text: `ID: ${member.id}`,
        },
        timestamp: new Date(),
      },
    ],
  });
});

client.on('guildMemberRemove', async (member) => {
  const channelName = process.env.GOODBYE_CHANNEL || 'despedidas';
  const channel = member.guild.channels.cache.find(
    (ch) => ch.name === channelName
  );
  if (!channel) return;

  await channel.send({
    embeds: [
      {
        color: 0xff0000,
        title: '¡Hasta luego!',
        description: `${member.user.tag} ha salido del servidor.`,
        thumbnail: {
          url: member.user.displayAvatarURL({ dynamic: true, size: 512 }),
        },
        fields: [
          {
            name: 'Miembros restantes',
            value: `${member.guild.memberCount}`,
            inline: true,
          },
        ],
        footer: {
          text: `ID: ${member.id}`,
        },
        timestamp: new Date(),
      },
    ],
  });
});

client.login(process.env.DISCORD_TOKEN);
