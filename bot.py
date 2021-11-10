import discord
import random
import asyncio
import os
import sys
import platform
from discord import guild

from discord.ext.commands import Bot
from discord.ext import commands

project_root = os.path.dirname(os.path.dirname(__file__))
if not os.path.isfile(f"{project_root}/Klaue/config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

#Ideen: Watch2Gether Link Posten. Bud Spencer und Terminator und Shax Sprüche
"""	
Setup bot intents (events restrictions)
For more information about intents, please go to the following websites:
https://discordpy.readthedocs.io/en/latest/intents.html
https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents
Default Intents:
intents.messages = True
intents.reactions = True
intents.emojis = True
intents.bans = True
intents.guild_typing = False
intents.typing = False
intents.dm_messages = False
intents.dm_reactions = False
intents.dm_typing = False
intents.guild_messages = True
intents.guild_reactions = True
intents.integrations = True
intents.invites = True
intents.voice_states = False
intents.webhooks = False
Privileged Intents (Needs to be enabled on dev page):
intents.presences = True
intents.members = True
"""
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True
bot = Bot(command_prefix=config.BOT_PREFIX, intents=intents)

# The code in this even is executed when the bot is ready
@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")


# Setup the game status task of the bot
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game("mit dir!"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Game("mit Knochen!"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Game(f"{config.BOT_PREFIX} prefix"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Game("mit Menschen!"))
        await asyncio.sleep(60)

# Removes the default help command of discord.py to be able to create our custom help command.
bot.remove_command("help")

if __name__ == "__main__":
    for extension in config.STARTUP_COGS:
        try:
            bot.load_extension(extension)
            extension = extension.replace("cogs.", "")
            print(f"Loaded extension '{extension}'")
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            extension = extension.replace("cogs.", "")
            print(f"Failed to load extension {extension}\n{exception}")

# The code in this event is executed every time someone sends a message, with or without the prefix
@bot.event
async def on_message(message):
    # Ignores if a command is being executed by a bot or by the bot itself
    if message.author == bot.user or message.author.bot:
        return
    else:
        if message.author.id not in config.BLACKLIST:
            # Process the command if the user is not blacklisted
            await bot.process_commands(message)
        else:
            # Send a message to let the user know he's blacklisted
            context = await bot.get_context(message)
            embed = discord.Embed(
                title="You're blacklisted!",
                description="Ask the owner to remove you from the list if you think it's not normal.",
                color=0x00FF00
            )
            await context.send(embed=embed)

@bot.event
async def on_raw_reaction_add(payload):        
    channel_id = payload.channel_id
    if channel_id in config.ROLE_CHANNELS:        
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        if guild is not None:
            member_id = payload.user_id    
            member = discord.utils.find(lambda m : m.id == member_id, guild.members)         
            if member is not None:              
                if payload.emoji.name == '💿':            
                    role = discord.utils.get(guild.roles, name="DJ")     
                    await discord.Member.add_roles(member, role)
                if payload.emoji.name == '👾':            
                    role = discord.utils.get(guild.roles, name="RGZ")     
                    await discord.Member.add_roles(member, role)
                if payload.emoji.name == '🐉':            
                    role = discord.utils.get(guild.roles, name="MH")     
                    await discord.Member.add_roles(member, role)
                if payload.emoji.name == '👽':            
                    role = discord.utils.get(guild.roles, name="D2")     
                    await discord.Member.add_roles(member, role)
                if payload.emoji.name == '🍺':            
                    role = discord.utils.get(guild.roles, name="Community Mitglied")     
                    await discord.Member.add_roles(member, role)
                if payload.emoji.name == '🏹':            
                    role = discord.utils.get(guild.roles, name="TESO")     
                    await discord.Member.add_roles(member, role)
                         
#Get reaction remove Events
@bot.event
async def on_raw_reaction_remove(payload):
    channel_id = payload.channel_id
    if channel_id in config.ROLE_CHANNELS:        
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        if guild is not None:
            member_id = payload.user_id    
            member = discord.utils.find(lambda m : m.id == member_id, guild.members)         
            if member is not None:
                if payload.emoji.name == '💿':            
                    role = discord.utils.get(guild.roles, name="DJ")     
                    await discord.Member.remove_roles(member, role)
                if payload.emoji.name == '👾':            
                    role = discord.utils.get(guild.roles, name="RGZ")     
                    await discord.Member.remove_roles(member, role)
                if payload.emoji.name == '🐉':            
                    role = discord.utils.get(guild.roles, name="MH")     
                    await discord.Member.remove_roles(member, role)
                if payload.emoji.name == '👽':            
                    role = discord.utils.get(guild.roles, name="D2")     
                    await discord.Member.remove_roles(member, role)
                if payload.emoji.name == '🍺':            
                    role = discord.utils.get(guild.roles, name="Community Mitglied")     
                    await discord.Member.remove_roles(member, role)
                if payload.emoji.name == '🏹':            
                    role = discord.utils.get(guild.roles, name="TESO")     
                    await discord.Member.remove_roles(member, role)

# The code in this event is executed every time a command has been *successfully* executed
@bot.event
async def on_command_completion(ctx):
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    print(
        f"Executed {executedCommand} command in {ctx.guild.name} by {ctx.message.author} (ID: {ctx.message.author.id})")

# The code in this event is executed every time a valid commands catches an error
@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title="Error!",
            description="This command is on a %.2fs cooldown" % error.retry_after,
            color=0x00FF00
        )
        await context.send(embed=embed)
    raise error

# Run the bot with the token
bot.run(config.TOKEN)