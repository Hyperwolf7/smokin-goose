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
insults = ["You're the type of person to like the warm side of the pillow.", "You're the human equivalent of a participation award.", "You’re the definition of a birth defect.", "You have small pp.", "You are as useful as a white crayon.", "If your mom drops you off at school its considered littering.", "You are a waste of sperm, your mom should have swallowed.", "You're the type of person to fall in the shower and try to use the water to get back up.", "You're the type of person to break friendships over pineapples on pizza.","You're a bitch and you know it.","You're the type of person to say things like lol and lmao in a real life conversation.","Your brain is lighter than gas.","Your IQ is lower than the melting point of helium.","Your iq is equivalent to your dick size in inches, and I can't see your dick.","You are so fat that thanos had to snap twice just for you.","I wonder how living the life of a hoe would be like, inform me.","If stupidity was a currency you would be rich.","Your brain is the one body part you don't have.","Your mom should have asked your dad to pull out.","Your own parents would rather have you hide in your room than interact with you.","You are the type of person to not click skip ad."]
smokin_goose = "Smokin' Goose bot was created on July 12th 2021. Created by Hyperwolf#2525."
invite_link = "https://discord.com/api/oauth2/authorize?client_id=864266661824692256&permissions=67226817&scope=bot"
discord_link = "Join the support server here: https://discord.gg/q6smjcsKZ5"
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


embed=discord.Embed(title="Commands:", description="A list of all the commands will be shown below.", color=0x00ffff)
embed.set_author(name="Smokin' Goose", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBjrw3JnC6dABO3jnLvizGcpGQrn3bek812g&usqp=CAU")
embed.add_field(name="quote", value="Shows a quote from a famous person.", inline=False)
embed.add_field(name="insult", value="Shows an insult. Some insults are user submitted insults. Join the support server to suggest more insults.", inline=False)
embed.add_field(name="info", value="Shows information about the bot.", inline=False)
embed.add_field(name="coinflip", value="Flips a coin with 2 sides, Heads, or Tails", inline=False)
embed.add_field(name="invite", value="Sends the invite link in order to invite the bot to your server.", inline=False)
embed.add_field(name="rndltr", value="Randomly generates a letter of the English alphabet.", inline=False)
embed.add_field(name="rolld6", value="Rolls a dice with 6 sides.", inline=False)
embed.add_field(name="rolld20", value="Rolls a dice with 20 sides.", inline=False)
embed.add_field(name="help", value="Shows this message.", inline=False)
embed.add_field(name="support", value="Sends the discord invite link to the support server.", inline=False)
embed.add_field(name="word", value="Sends a random word.", inline=False)
embed.add_field(name="vote", value="Sends the top.gg bot voting link.", inline=False)
embed.add_field(name="servers", value="See how many servers SGB is in.", inline=False)
embed.add_field(name="status", value="See if the bot is on or not.", inline=False)

@bot.command()
async def test(ctx):
	await ctx.send("test command")

@bot.command()
async def insult(ctx):
  insult = get_insult()
  await ctx.send(insult) or await ctx.send(insults)

@bot.command()
async def help(ctx):
  await ctx.send(embed=embed)

@bot.command()
async def quote(ctx):
  quote = get_quote()
  await ctx.send(quote)

@bot.command()
async def coinflip(ctx):
  await ctx.send(random.choice(flip_a_coin))

@bot.command()
async def invite(ctx):
  await ctx.send(invite_link)

@bot.command()
async def rndltr(ctx):
  await ctx.send(random.choice(letters))

@bot.command()
async def rolld6(ctx):
  await ctx.send((random.randint(1,6)))

@bot.command()
async def rolld20(ctx):
  await ctx.send((random.randint(1,20)))

@bot.command()
async def support(ctx):
  await ctx.send(discord_link)

@bot.command()
async def info(ctx):
  await ctx.send(smokin_goose)

@bot.command()
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
      await ctx.send('Placeholder')
    else:
      await ctx.send('Access denied, only [Bot Owner] can use this command.')

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

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="https://discord.gg/q6smjcsKZ5"))

  print('Servers connected to:')
  for guild in bot.guilds:
      print(guild.name)


keep_alive()
bot.run(os.getenv('TOKEN'))
