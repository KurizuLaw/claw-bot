import os
import sys
import discord
import platform
import random
from discord.ext import commands

project_root = os.path.dirname(os.path.dirname(__file__))
if not os.path.isfile(f"{project_root}/config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

MAIQ = ["Dieser Lügt nicht","Maiq ist kein Lügner"]

class Klaue(commands.Cog, name="klaue"):
    def __init__(self, bot):
        self.bot = bot
    
    #@commands.command(name="liste")
    #async def list(self, context, *args):
        """
        Erstelle einen Liste bei der man sich eintragen kann.
        """
        #https://stackoverflow.com/questions/63078283/add-users-who-react-to-reaction-to-embed
        #Adaptieren
        #https://www.youtube.com/watch?v=MgCJG8kkq50
        #raid_entry = " ".join(args)        
        #embed = discord.Embed(            
        #    title=f"Liste: {raid_entry}",
        #    description=f"Teilnehmer:\n",
        #    color=0xff8800
        #)        
        #embed.set_footer(
        #    text=f"Eine neuee Liste wurde von {context.message.author} erstellt, • React zum Beitritt!"
        #)        
        #embed_message = await context.send(embed=embed)
        #await embed_message.add_reaction("👍")        
        #await embed_message.add_reaction("🤷")
        #await context.message.delete()    
    
def setup(bot):
    bot.add_cog(Klaue(bot))