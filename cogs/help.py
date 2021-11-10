import os
import sys
import discord
from discord.ext import commands

project_root = os.path.dirname(os.path.dirname(__file__))
if not os.path.isfile(f"{project_root}/config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config


class Help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, context):
        """
        Liste alle Komandos die dem Bot bekannt sind.
        """
        prefix = config.BOT_PREFIX
        if not isinstance(prefix, str):
            prefix = prefix[0]
        embed = discord.Embed(
            title="Help", description="Liste der verfügbaren Komandos:", color=0x00FF00)
        for i in self.bot.cogs:
            cog = self.bot.get_cog(i.lower())
            commands = cog.get_commands()
            command_list = [command.name for command in commands]
            command_description = [command.help for command in commands]
            help_text = '\n'.join(
                f'{prefix}{n} - {h}' for n, h in zip(command_list, command_description))
            embed.add_field(name=i.capitalize(),
                            value=f'```{help_text}```', inline=False)
        await context.send(embed=embed)
        await context.message.delete()


def setup(bot):
    bot.add_cog(Help(bot))
