import discord
from discord.ext import commands
import whois21
from ping import Ping

# ---------- USER CONFIGURABLE SECTION -----------------
token = ''  # Stores the bot's token. Used to pass the bot's token into bot.run in order to run the bot.
bot = commands.Bot(command_prefix='', intents=discord.Intents.all())  # Changing the bot's intents will break functionality! Only touch this if you know what you're doing!
bot.Prefix = '!'  # Defines the bot's command prefix.
# ---------- END OF USER CONFIGURABLE SECTION ----------

@bot.event  # Initializes a bot event.
async def on_message(message):  # Runs the code whenever a message is sent in the server.
    args = str(message.content).lower().split(' ')
    if args[0] == bot.Prefix + 'check':
        msg = str(message.content)
        if msg.find('/'):
            domain = msg.lower().split('/')
            whois = whois21.WHOIS(domain[2])
            if whois.success:
                ping = Ping()
                ping.ping(domain[2])
                if ping.returncode == 0:
                    dataEmbed = discord.Embed(title='Link Status', description='**' + domain[2] + ' is active.**', color=0x2f3136)
                    await message.channel.send(embed=dataEmbed)  # Sends the embed from dataEmbed in the channel the command was triggered in.

bot.run(token)  # Passes is in the token from the token variable and runs the bot.