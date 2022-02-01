import discord
from discord.ext import commands


client = discord.Client()


names = [
    "Hitagi",
 "Senjougahara",
  "Hanekawa", 
  "Tsubasa", "Koyomi", 
  "Araragi", "Karen", 
  "Tsukihi", 
  "Hachikuji", 
  "Mayoi", 
  "Yozuru", 
  "Kagenui", 
  "Gaen", 
  "Izuko", 
  "Tadatsuru", 
  "Teori", 
  "Yotsugi", 
  "Ononoki", 
  "Oshino", 
  "Ougi", 
  "Shinobu", 
  "Meme", 
  "Monogatari", 
  "Testarossa",
  "Kiss-Shot Acerola-Orion Heart-Under-Blade",
  "Kaiki",
  "Deishuu", 
  "Sengoku", 
  "Nadeko", 
  "Sodachi", 
  "Oikura", 
  "Ougi", 
  "Guillotine", 
  "Cutter", 
  "Rouka", 
  "Numachi"]

@client.event
async def on_ready():
    print("Logged in, sniping current keywords: ")
    print(*names, sep = "\n")

@client.event
async def on_message(message):
    if message.author.id == 432610292342587392:
        if message.embeds:
            for name in names:
                if name in message.embeds[0].author.name:
                    await message.add_reaction("✅")
                    print(message.embeds[0].author.name)
                    print("-------")

client.run("token")