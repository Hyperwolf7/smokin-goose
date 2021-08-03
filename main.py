import discord
import os
import requests
import json
import random
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix = "sg!")
bot.remove_command('help')

flip_a_coin = ["Heads", "Tails"]
insults = ["You're the type of person to like the warm side of the pillow.", "You're the human equivalent of a participation award.", "You’re the definition of a birth defect.", "You have small pp.", "You are as useful as a white crayon.", "If your mom drops you off at school its considered littering.", "You are a waste of sperm, your mom should have swallowed.", "You're the type of person to fall in the shower and try to use the water to get back up.", "You're the type of person to break friendships over pineapples on pizza.","You're a bitch and you know it.","You're the type of person to say things like lol and lmao in a real life conversation.","Your brain is lighter than gas.","Your IQ is lower than the melting point of helium.","Your iq is equivalent to your dick size in inches, and I can't see your dick.","You are so fat that thanos had to snap twice just for you.","I wonder how living the life of a hoe would be like, inform me.","If stupidity was a currency you would be rich.","Your brain is the one body part you don't have.","Your mom should have asked your dad to pull out.","Your own parents would rather have you hide in your room than interact with you.","You are the type of person to not click skip ad.","Even flat-earthers and anti-vaxxers have a difficult time trying to understand the bullsh*t you say.","World hunger would end if you stop eating."]
smokin_goose = "Smokin' Goose bot was created on July 12th 2021. Created by Hyperwolf#2525."
invite_link = "https://discord.com/api/oauth2/authorize?client_id=864266661824692256&permissions=67226817&scope=bot"
discord_link = "Join the support server here: https://discord.gg/q6smjcsKZ5"
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


embed=discord.Embed(title="Commands:", description="Type sg!helpcat [category] for commands on the specific category.", color=0x00ffff)
generateembed=discord.Embed(title="Generate", description="Below are a list of commands that generate something.", color=0x00ffff)
miscembed=discord.Embed(title="Misc", description="Below are a list of commands that don't fit in another category.", color=0x00ffff)
randomembed=discord.Embed(title="Random", description="Below are a list of commands that randomly generate something", color=0x00ffff)
actionembed=discord.Embed(title="Action", description="Below are a list of commands that do something with the goose.", color=0x00ffff)
mathembed=discord.Embed(title="Math", description="Below are a list of commands that do math.", color=0x00ffff)

embed.set_author(name="Smokin' Goose", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBjrw3JnC6dABO3jnLvizGcpGQrn3bek812g&usqp=CAU")
generateembed.set_author(name="Smokin' Goose", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBjrw3JnC6dABO3jnLvizGcpGQrn3bek812g&usqp=CAU")
miscembed.set_author(name="Smokin' Goose", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBjrw3JnC6dABO3jnLvizGcpGQrn3bek812g&usqp=CAU")
randomembed.set_author(name="Smokin' Goose", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBjrw3JnC6dABO3jnLvizGcpGQrn3bek812g&usqp=CAU")
actionembed.set_author(name="Smokin' Goose", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBjrw3JnC6dABO3jnLvizGcpGQrn3bek812g&usqp=CAU")
mathembed.set_author(name="Smokin' Goose", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBjrw3JnC6dABO3jnLvizGcpGQrn3bek812g&usqp=CAU")

generateembed.add_field(name="quote", value="Shows a quote from a famous person.", inline=False)
generateembed.add_field(name="insult", value="Shows an insult. Some insults are user submitted insults. Join the support server to suggest more insults.", inline=False)
generateembed.add_field(name="word", value="Sends a random word.", inline=False)
generateembed.add_field(name="isslocation", value="Get the longitude and latitude of the ISS (International Space Station) at the current time.", inline=False)
generateembed.add_field(name="goose", value="Generate a random goose picture.", inline=False)
generateembed.add_field(name="joke", value="Generate a random joke.", inline=False)
miscembed.add_field(name="info", value="Shows information about the bot.", inline=False)
miscembed.add_field(name="invite", value="Sends the invite link in order to invite the bot to your server.", inline=False)
miscembed.add_field(name="help", value="Shows this message.", inline=False)
miscembed.add_field(name="support", value="Sends the discord invite link to the support server.", inline=False)
miscembed.add_field(name="vote", value="Sends the top.gg bot voting link.", inline=False)
miscembed.add_field(name="servers", value="See how many servers SGB is in.", inline=False)
miscembed.add_field(name="status", value="See if the bot is on or not.", inline=False)
randomembed.add_field(name="coinflip", value="Flips a coin with 2 sides, Heads, or Tails", inline=False)
randomembed.add_field(name="rndltr", value="Randomly generates a letter of the English alphabet.", inline=False)
randomembed.add_field(name="roll", value="Rolls a dice with a custom number of sides. sg!roll [# of sides]", inline=False)
actionembed.add_field(name="say", value="Make the bot say whatever you want. sg!say [message]", inline=False)
actionembed.add_field(name="petgoose", value="Pet the Smokin Goose.", inline=False)
mathembed.add_field(name="add", value="Addition, sg!add [value1] [value2]", inline=False)
mathembed.add_field(name="sub", value="Subtraction of value 2 from value 1, sg!sub [value1] [value2]", inline=False)
mathembed.add_field(name="multi", value="Multiplication, sg!multi [value1] [value2]", inline=False)
mathembed.add_field(name="div", value="Division of value 1 by value 2 sg!div [value1] [value2]", inline=False)
mathembed.add_field(name="pwr", value="Value 1 to the power of value 2, sg!pwr [value1] [value2]", inline=False)
mathembed.add_field(name="root", value="The value 2 root of value 1, sg!root [value1] [value2]", inline=False)
embed.add_field(name="Generate", value="Commands that generate things, ex. quote", inline=False)
embed.add_field(name="Random", value="Random generation commands", inline=False)
embed.add_field(name="Action", value="Things you can do with the bot", inline=False)
embed.add_field(name="Misc", value="Various commands that do not fit into any other categories", inline=False)
embed.add_field(name="Math", value="Commands that help you do math", inline=False)
embed.set_footer(text="Note: Smokin' Goose Bot and its creator does not promote smoking or vaping in any way.")

@bot.command()
async def test(ctx):
	await ctx.send("test command")

@bot.command()
@commands.cooldown(1, 3,commands.BucketType.user)
async def insult(ctx):
  insult = get_insult()
  await ctx.send(insult) or await ctx.send(insults)

@bot.command()
async def helpcat(ctx, cat:str):
  if cat.endswith('generate'):
    await ctx.send(embed=generateembed)
  elif cat.endswith('random'):
    await ctx.send(embed=randomembed)
  elif cat.endswith('misc'):
    await ctx.send(embed=miscembed)
  elif cat.endswith('math'):
    await ctx.send(embed=mathembed)
  elif cat.endswith('action'):
    await ctx.send(embed=actionembed)

@bot.command()
async def help(ctx):
  await ctx.send (embed=embed)

@bot.command()
@commands.cooldown(1, 3,commands.BucketType.user)
async def quote(ctx):
  quote = get_quote()
  await ctx.send(quote)

@bot.command()
@commands.cooldown(1, 3,commands.BucketType.user)
async def coinflip(ctx):
  await ctx.send(random.choice(flip_a_coin))

@bot.command()
async def invite(ctx):
  await ctx.send(invite_link)

@bot.command()
@commands.cooldown(1, 3,commands.BucketType.user)
async def rndltr(ctx):
  await ctx.send(random.choice(letters))

@bot.command()
@commands.cooldown(1, 3,commands.BucketType.user)
async def roll(ctx, a:int):
  await ctx.send((random.randint(1,a)))

@bot.command()
async def support(ctx):
  await ctx.send(discord_link)

@bot.command()
async def info(ctx):
  await ctx.send(smokin_goose)

@bot.command()
@commands.cooldown(1, 3,commands.BucketType.user)
async def word(ctx):
  word = get_word()
  await ctx.send(word)

@bot.command()
async def servers(ctx):
  servers = list(bot.guilds)
  await ctx.send(f"SGB is connected on {str(len(servers))} servers")

@bot.command()
async def vote(ctx):
  await ctx.send("top.gg: https://top.gg/bot/864266661824692256/vote \ndiscordbotlist.com: https://discordbotlist.com/bots/smokin-goose/upvote")

@bot.command()
async def status(ctx):
  await ctx.send("If you see this message, the bot is currently online.")

@bot.command()
async def owneronly(ctx):
    yourID = 282949765161811968
    if ctx.message.author.id == yourID:
      await ctx.send('Hyperwolf said this message.')
    else:
      await ctx.send('Access denied, only [Bot Owner] can use this command.')

@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def petgoose(ctx):
    await ctx.send('You have petted the Smokin Goose.')

@bot.command()
@commands.cooldown(1, 5,commands.BucketType.user)
async def say(ctx, message=None):
    await ctx.send(message)

@bot.command()
@commands.cooldown(1, 3,commands.BucketType.user)
async def add(ctx,a:int,b:int): 
    await ctx.send(f"{a} + {b} = {a+b}") 

@bot.command() 
@commands.cooldown(1, 3,commands.BucketType.user)
async def sub(ctx,a:int,b:int): 
    await ctx.send(f"{a} - {b} = {a-b}") 

@bot.command()
@commands.cooldown(1, 3,commands.BucketType.user) 
async def multi(ctx,a:int,b:int): 
    await ctx.send(f"{a} * {b} = {a*b}")

@bot.command()
@commands.cooldown(1, 3,commands.BucketType.user) 
async def div(ctx,a:int,b:int): 
  if b == 0 :
    await ctx.send('undefined')
  else:
    await ctx.send(f"{a} / {b} = {a/b}")

@bot.command()
@commands.cooldown(1, 3,commands.BucketType.user) 
async def pwr(ctx,a:int,b:int): 
    await ctx.send(f"{a} ** {b} = {a**b}")

@bot.command()
@commands.cooldown(1, 3,commands.BucketType.user)
async def root(ctx,a:int,b:int):
  if a < 0:
    await ctx.send('imaginary number')
  else:
    await ctx.send(f"{a} ** (1/{b}) = {a**(1/b)}")

@bot.command()
@commands.cooldown(1, 3,commands.BucketType.user)
async def goose(ctx):
  duck = get_duck()
  await ctx.send(duck)

@bot.command()
@commands.cooldown(1, 1,commands.BucketType.user)
async def isslocation(ctx):
  iss = get_iss()
  await ctx.send(iss)

@bot.command()
@commands.cooldown(1,3,commands.BucketType.user)
async def joke(ctx):
  joke = get_joke()
  await ctx.send(joke)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data [0]['a']
  return(quote)

def get_insult():
  insult_response = requests.get("https://insult-api.amogus.workers.dev")
  insult_json_data = json.loads(insult_response.text)
  insult = insult_json_data['insult']
  return(insult)

def get_word():
  word_response = requests.get("https://random-words-api.vercel.app/word")
  word_json_data = json.loads(word_response.text)
  word = "Word: " + word_json_data[0]['word'] + "\nDefinition: " + word_json_data[0]['definition']
  return(word)

def get_duck():
  duck_response = requests.get("https://random-d.uk/api/v2/random")
  duck_json_data = json.loads(duck_response.text)
  duck = duck_json_data['url']
  return(duck)

def get_iss():
  iss_response = requests.get("http://api.open-notify.org/iss-now.json")
  iss_json_data = json.loads(iss_response.text)
  iss = iss_json_data['iss_position']
  return(iss)

def get_joke():
  joke_response = requests.get("https://official-joke-api.appspot.com/jokes/random")
  joke_json_data = json.loads(joke_response.text)
  joke = joke_json_data['setup'] + "\n" + "\n" + joke_json_data['punchline']
  return(joke)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown, you can use it in {round(error.retry_after, 2)} seconds.')

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="https://discord.gg/q6smjcsKZ5"))

  print('Servers connected to:')
  for guild in bot.guilds:
      print(guild.name)


keep_alive()
bot.run(os.getenv('TOKEN'))
