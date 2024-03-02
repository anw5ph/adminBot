import os
from dotenv import load_dotenv

import discord
from discord import app_commands
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
EXPERIENCE_ROLES_MESSAGE = int(os.getenv('EXPERIENCE_ROLES_MESSAGE'))
LANGUAGES_ROLES_MESSAGE = int(os.getenv('LANGUAGES_ROLES_MESSAGE'))


bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

# Initialize adminBot
@bot.event
async def on_ready():
    try:
        sync = await bot.tree.sync()

    except Exception as e:
        print(e)

# Create new channel on the server when requested
@bot.tree.command(name='create-channel')
@commands.has_role('Admin')
@app_commands.describe(arg = "What should I name the channel?")
async def create_channel(interaction: discord.Interaction, arg: str):
    guild = interaction.guild
    existing_channel = discord.utils.get(guild.channels, name=arg)
    if not existing_channel:
        await guild.create_text_channel(arg)
        await interaction.response.send_message(f"Channel named `{arg}` was successfully created!")

# Add role to user when reaction is added
@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id != EXPERIENCE_ROLES_MESSAGE and payload.message_id != LANGUAGES_ROLES_MESSAGE:
        return 
    
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    
    # Experience Roles
    if payload.message_id == EXPERIENCE_ROLES_MESSAGE:
        if payload.emoji.name == "🗡️":
            role = discord.utils.get(member.guild.roles, name="Recruit")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "🛡️":
            role = discord.utils.get(member.guild.roles, name="Brigade")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "⚔️":
            role = discord.utils.get(member.guild.roles, name="Elite")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "🏰":
            role = discord.utils.get(member.guild.roles, name="Legendary")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")

    # Programming Language Roles
    if payload.message_id == LANGUAGES_ROLES_MESSAGE:
        if payload.emoji.name == "🐍":
            role = discord.utils.get(member.guild.roles, name="Python")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "☕":
            role = discord.utils.get(member.guild.roles, name="Java")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "🕸️":
            role = discord.utils.get(member.guild.roles, name="JavaScript")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "➕":
            role = discord.utils.get(member.guild.roles, name="C++")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "🔷":
            role = discord.utils.get(member.guild.roles, name="C#")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "📘":
            role = discord.utils.get(member.guild.roles, name="TypeScript")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "🐘":
            role = discord.utils.get(member.guild.roles, name="PHP")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "🐦":
            role = discord.utils.get(member.guild.roles, name="Swift")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "💎":
            role = discord.utils.get(member.guild.roles, name="Ruby")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "🚀":
            role = discord.utils.get(member.guild.roles, name="Go")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "⚰️":
            role = discord.utils.get(member.guild.roles, name="C")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "🎯":
            role = discord.utils.get(member.guild.roles, name="Dart")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")
        elif payload.emoji.name == "🌐":
            role = discord.utils.get(member.guild.roles, name="HTML/CSS")
            if role not in member.roles:
                await member.add_roles(role)
                print(f"{role} role added to {member}")


# Remove roles when reaction is removed
@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id != EXPERIENCE_ROLES_MESSAGE and payload.message_id != LANGUAGES_ROLES_MESSAGE:
        return 
    
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    # Experience Roles
    if payload.message_id == EXPERIENCE_ROLES_MESSAGE:
        if payload.emoji.name == "🗡️":
            role = discord.utils.get(member.guild.roles, name="Recruit")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "🛡️":
            role = discord.utils.get(member.guild.roles, name="Brigade")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "⚔️":
            role = discord.utils.get(member.guild.roles, name="Elite")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "🏰":
            role = discord.utils.get(member.guild.roles, name="Legendary")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")

    # Programming Language Roles
    if payload.message_id == LANGUAGES_ROLES_MESSAGE:
        if payload.emoji.name == "🐍":
            role = discord.utils.get(member.guild.roles, name="Python")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "☕":
            role = discord.utils.get(member.guild.roles, name="Java")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "🕸️":
            role = discord.utils.get(member.guild.roles, name="JavaScript")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "➕":
            role = discord.utils.get(member.guild.roles, name="C++")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "🔷":
            role = discord.utils.get(member.guild.roles, name="C#")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "📘":
            role = discord.utils.get(member.guild.roles, name="TypeScript")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "🐘":
            role = discord.utils.get(member.guild.roles, name="PHP")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "🐦":
            role = discord.utils.get(member.guild.roles, name="Swift")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "💎":
            role = discord.utils.get(member.guild.roles, name="Ruby")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "🚀":
            role = discord.utils.get(member.guild.roles, name="Go")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "⚰️":
            role = discord.utils.get(member.guild.roles, name="C")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "🎯":
            role = discord.utils.get(member.guild.roles, name="Dart")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")
        elif payload.emoji.name == "🌐":
            role = discord.utils.get(member.guild.roles, name="HTML/CSS")
            if role in member.roles:
                await member.remove_roles(role)
                print(f"{role} role removed from {member}")

# Run adminBot
bot.run(TOKEN)