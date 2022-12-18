import discord
from discord.ext import commands, tasks
import requests
import time



token = 'token here'

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.members = True
intents.messages = True
client = commands.Bot(command_prefix="*",help_command=None, status=discord.Status.idle, intents=intents)

owner = 1002273340372820038 

@client.event
async def on_ready():
  print(''' 
                    _           _                 _ _              _ 
                   | |__   ___ | |_    ___  _ __ | (_)_ __   ___  | |
                   | '_ \ / _ \| __|  / _ \| '_ \| | | '_ \ / _ \ | |
                   | |_) | (_) | |_  | (_) | | | | | | | | |  __/ |_|
                   |_.__/ \___/ \__|  \___/|_| |_|_|_|_| |_|\___| (_)
                       ________________________________________
                      |                       |                |
                      | Bot dev by > xara ~$  |  --> V 2.0 <-- |
                      |_______________________|________________|
                                       _________
                                      |Bot error|
 ''')
  await client.change_presence(activity = discord.Streaming(name = 
    "Dev By > xara ~$", url = "https://twitch.tv/xara_01"))
  STATUS.start()


@client.command()
async def ping(ctx):
  embed = discord.Embed(
    title=f"⭐ Bot ping ⭐",
    description=f"*__**Pong !**__*   `{round(client.latency * 1000)}` ms 🏓",
    color=0x00000F)
  embed.set_thumbnail(
    url=
    "https://cdn.discordapp.com/attachments/1044571176116166717/1044575061836832798/mp4.gif"
  )
  await ctx.send(embed=embed)


@client.command()
async def help(ctx):
  embed = discord.Embed(
    title="⭐ Help ⭐",
    description="*The Bot has bene created by **> xara ~$#0001*** \n",
    color=0x00000F)
  embed.set_author(
    name="github.com/xara-01",
    icon_url=
    "https://cdn.discordapp.com/attachments/972965986766557215/1030965023436177408/darck_pp.png"
  )
  embed.set_image(
    url=
    "https://cdn.discordapp.com/attachments/972965986766557215/1052980923609665546/gang.gif"
  )
  embed.set_thumbnail(
    url=
    "https://cdn.discordapp.com/attachments/1044571176116166717/1044575061836832798/mp4.gif"
  )
  embed.add_field(
    name="*__!ipinfo__*",
    value=
    "*__give the ip info.__*",
    inline=True)
  embed.add_field(
    name="*__!ping__*",
    value=
    "*__give the ping of the bot.__*",
    inline=True)
  embed.add_field(
    name="*__!clear__*",
    value=
    "*__Clear message.__*",
    inline=False)

  embed.timestamp = ctx.message.created_at
  await ctx.send(embed=embed)




@client.event
async def on_message(message):
    if message.content.startswith("!clear"):
        if not message.author.guild_permissions.manage_messages:
            await message.channel.send("_**__You don't have permission to use this command.__**_")
            return

        num_messages = int(message.content.split()[1])
        await message.channel.purge(limit=num_messages)









@client.command()
async def ipinfo(ctx, ip_address):
  # Use the ipinfo.io API to retrieve information about the IP address
  response = requests.get(f"https://ipinfo.io/{ip_address}/json")
  data = response.json()
  ipp = data["ip"]
  # Create an embed using the information retrieved from the API
  embed = discord.Embed(title=f"⭐ IP Address Information [{ipp}] ⭐", description='🕷' ,color=0x00000F)
  embed.add_field(name="🌆 City", value=data["city"])
  embed.add_field(name="🔎 Region", value=data["region"])
  embed.add_field(name="🏙 Country", value=data["country"])
  embed.add_field(name="💉 Organization", value=data["org"])
  embed.add_field(name="🛫 Zip Code", value=data["postal"])
  embed.add_field(name="⏲ Time Zone", value=data["timezone"], inline=False)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1044571176116166717/1044575061836832798/mp4.gif")
  embed.set_image(url="https://cdn.discordapp.com/attachments/972965986766557215/1052980923609665546/gang.gif")
  embed.set_author(name="github.com/xara-01",icon_url="https://cdn.discordapp.com/attachments/972965986766557215/1030965023436177408/darck_pp.png")
  embed.timestamp = ctx.message.created_at
  
  # Send the embed as a response to the command
  await ctx.send(embed=embed)


#status loop

@tasks.loop(seconds=5)
async def STATUS():
  await client.change_presence(activity = discord.Streaming(name = 
    "Dev By > xara ~$", url = "https://twitch.tv/_sky.os_"))
  time.sleep(1)
  await client.change_presence(activity = discord.Streaming(name="!help", url = "https://twitch.tv/_sky.os_"))

client.run(token)