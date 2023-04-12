import discord
from discord.ext import commands
from discord import Member
from replit import db
from keep_alive import keep_alive

TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "YOUR_CHANNEL_ID"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')


@bot.event
async def on_message(message):

  if message.channel.id == CHANNEL_ID:

    if message.author.status == discord.Status.offline:

      await message.delete()
      channel = bot.get_channel(message.channel.id)
      await channel.send(message.author.name +", you have to be connected to send a message")

  await bot.process_commands(message)


@bot.event
async def on_voice_state_update(member, before, after):
  if before.channel is None and after.channel is not None:
    if member.status == discord.Status.offline:
      await member.move_to(None)
      sensaciones = bot.get_channel(CHANNEL_ID)
      await sensaciones.send(member.name +", you have to be connected to join a voice channel")


@bot.event
async def on_presence_update(before, after):
  if before.status is discord.Status.online and after.status is discord.Status.offline:
    # changed from online to offline
    if after.voice is not None:
      await after.move_to(None)
      sensaciones = bot.get_channel(CHANNEL_ID)
      await sensaciones.send(before.name + ", you cant be on a voice chat while being disconnected")


keep_alive()
bot.run(TOKEN)