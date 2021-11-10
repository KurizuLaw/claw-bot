import os
import sys
import discord
from discord.ext import commands

project_root = os.path.dirname(os.path.dirname(__file__))
if not os.path.isfile(f"{project_root}/config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config


class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', pass_context=True)
    async def kick(self, context, member: discord.Member, *args):
        """
        Kick einen Nutzer vom Server.
        """
        if context.message.author.guild_permissions.kick_members:
            if member.guild_permissions.administrator:
                embed = discord.Embed(
                    title="Fehler!",
                    description="Du kannst Admins nicht kicken.",
                    color=0x00FF00
                )
                await context.send(embed=embed)
                await context.message.delete()
            else:
                try:
                    reason = " ".join(args)
                    embed = discord.Embed(
                        title="Nutzer gekickt!",
                        description=f"**{member}** wurde von **{context.message.author}** gekickt!",
                        color=0x00FF00
                    )
                    embed.add_field(
                        name="Grund:",
                        value=reason
                    )
                    await context.send(embed=embed)
                    await context.message.delete()
                    try:
                        await member.send(
                            f"Nutzer wurde von **{context.message.author}** gekickt!\nGrund: {reason}"
                        )
                    except:
                        pass
                except:
                    embed = discord.Embed(
                        title="Fehler!",
                        description="Währende des Versuchs den Nutzer zu kicken ist ein Fehler aufgetreten.",
                        color=0x00FF00
                    )
                    await context.message.channel.send(embed=embed)
                    await context.message.delete()
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast nicht die Berechtigung dieses Kommando auszuführen.",
                color=0x00FF00
            )
            await context.send(embed=embed)
            await context.message.delete()

    @commands.command(name="nick")
    async def nick(self, context, member: discord.Member, *, name: str):
        """
        Ändere den Nickname eines Nutzers auf diesem Server.
        """
        if context.message.author.guild_permissions.administrator:
            try:
                if name.lower() == "!reset":
                    name = None
                embed = discord.Embed(
                    title="Nickname geändert!",
                    description=f"**{member}'s** neuer Nickname ist **{name}**!",
                    color=0x00FF00
                )
                await context.send(embed=embed)
                await member.change_nickname(name)
                await context.message.delete()
            except:
                embed = discord.Embed(
                    title="Fehler!",
                    description="Währende des Versuchs den Nickname zu ändern ist ein Fehler aufgetreten.",
                    color=0x00FF00
                )
                await context.message.channel.send(embed=embed)
                await context.message.delete()
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast nicht die Berechtigung dieses Kommando auszuführen.",
                color=0x00FF00
            )
            await context.send(embed=embed)
            await context.message.delete()

    @commands.command(name="ban")
    async def ban(self, context, member: discord.Member, *args):
        """
        Bannt einen Nutzer vom Server.
        """
        if context.message.author.guild_permissions.administrator:
            try:
                if member.guild_permissions.administrator:
                    embed = discord.Embed(
                        title="Fehler!",
                        description="Du kannst Admins nicht bannen.",
                        color=0x00FF00
                    )
                    await context.send(embed=embed)
                    await context.message.delete()
                else:
                    reason = " ".join(args)
                    embed = discord.Embed(
                        title="Nutzer gebannt!",
                        description=f"**{member}** wurde von **{context.message.author}** gebannt!",
                        color=0x00FF00
                    )
                    embed.add_field(
                        name="Grund:",
                        value=reason
                    )
                    await context.send(embed=embed)
                    await member.send(f"Du wurdest von **{context.message.author}** gebannt!\nGrund: {reason}")
                    await member.ban(reason=reason)
                    await context.message.delete()
            except:
                embed = discord.Embed(
                    title="Fehler!",
                    description="Während des Versuchs den Nutzer zu bannen ist ein Fehler aufgetreten.",
                    color=0x00FF00
                )
                await context.send(embed=embed)
                await context.message.delete()
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast nicht die Berechtigung dieses Kommando auszuführen.",
                color=0x00FF00
            )
            await context.send(embed=embed)
            await context.message.delete()

    @commands.command(name="warn")
    async def warn(self, context, member: discord.Member, *args):
        """
        Warne einen Nutzer über eine Privatnachricht.
        """
        if context.message.author.guild_permissions.administrator:
            reason = " ".join(args)
            embed = discord.Embed(
                title="Nutzer gewarnt!",
                description=f"**{member}** wurde von **{context.message.author}** gewarnt!",
                color=0x00FF00
            )
            embed.add_field(
                name="Grund:",
                value=reason
            )
            await context.send(embed=embed)
            await context.message.delete()
            try:
                await member.send(f"Du wurdest von **{context.message.author}** gewarnt!\nGrund: {reason}")                
            except:
                pass
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast nicht die Berechtigung dieses Kommando auszuführen.",
                color=0x00FF00
            )
            await context.send(embed=embed)
            await context.message.delete()

    @commands.command(name="note")
    async def note(self, context, member: discord.Member, *args):
        """
        Benachrichtige einen Nutzer über eine Privatnachricht.
        """
        if context.message.author.guild_permissions.administrator:
            reason = " ".join(args)
            embed = discord.Embed(
                title="Nutzer benachrichtigt!",
                description=f"**{member}** wurde von **{context.message.author}** benachrichtigt!",
                color=0x00FF00
            )
            embed.add_field(
                name="Nachricht:",
                value=reason
            )
            await context.send(embed=embed)
            await context.message.delete()
            try:
                await member.send(f"Du wurdest von Benachrichtigt **{context.message.author}**!\nNachricht: {reason}")
            except:
                pass
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast nicht die Berechtigung dieses Kommando auszuführen.",
                color=0x00FF00
            )
            await context.send(embed=embed)
            await context.message.delete()

    @commands.command(name="purge")
    async def purge(self, context, number):
        """
        Lösche eine Anzahl von Nachrichten.
        """
        if context.message.author.guild_permissions.administrator:
            
            purged_messages = await context.message.channel.purge(limit=int(number))
            embed = discord.Embed(
                title="Nachrichten gelöscht!",
                description=f"**{context.message.author}** hat **{len(purged_messages)}** Nachrichten gelöscht!",
                color=0x00FF00
            )
            await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast nicht die Berechtigung dieses Kommando auszuführen.",
                color=0x00FF00
            )
            await context.send(embed=embed)


def setup(bot):
    bot.add_cog(moderation(bot))
