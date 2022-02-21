import discord


client = discord.Client()

#name keywords (eg. "Hitagi Senjougahara" "Hitagi" "Senjougahara")
names = [
    "Hitagi",
 "Senjougahara",
  "Hanekawa", 
  "Tsubasa", 
  "Koyomi", 
  "Araragi", 
  "Karen", 
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

#Series
names2 = [
    "Nichijou",
    "Monogatari"
]

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
            for name in names2:
                if name in message.embeds[0].description:
                    await message.add_reaction("✅")
                    print(message.embeds[0].author.name)
                    print("-------")
                

client.run("Token")
