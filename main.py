import discord
import os
import requests
import json
import random
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix = "%")
bot.remove_command('help')

flip_a_coin = ["Heads", "Tails"]
insults = ["You're the type of person to like the warm side of the pillow.", "You're the human equivalent of a participation award.", "You’re the definition of a birth defect.", "You have small pp.", "You are as useful as a white crayon.", "If your mom drops you off at school its considered littering.", "You are a waste of sperm, your mom should have swallowed.", "You're the type of person to fall in the shower and try to use the water to get back up.", "You're the type of person to break friendships over pineapples on pizza."]
smokin_goose = "Smokin' Goose bot created on July 12th 2021. Created by Hyperwolf#2525."
invite_link = "Invite link currently unavaliable."
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


embed=discord.Embed(title="Commands:", description="A list of all the commands will be shown below.", color=0x00ffff)
embed.set_author(name="Smokin' Goose", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBjrw3JnC6dABO3jnLvizGcpGQrn3bek812g&usqp=CAU")
embed.add_field(name="%quote", value="Shows a quote from a famous person.", inline=False)
embed.add_field(name="%insult", value="Shows a user-suggested insult.", inline=False)
embed.add_field(name="%info", value="Shows information about the bot.", inline=False)
embed.add_field(name="%coinflip", value="Flips a coin with 2 sides, Heads, or Tails", inline=False)
embed.add_field(name="%invite", value="Sends the invite link in order to invite the bot to your server.", inline=False)
embed.add_field(name="%rndltr", value="Randomly generates a letter of the English alphabet.", inline=False)
embed.add_field(name="%rolld6", value="Rolls a dice with 6 sides.", inline=False)
embed.add_field(name="%rolld20", value="Rolls a dice with 20 sides.", inline=False)
embed.add_field(name="%help", value="Shows this message.", inline=False)


@bot.command()
async def test(ctx):
	await ctx.send("test command") #attempt at "say command"

@bot.command()
async def insult(ctx):
  await ctx.send(random.choice(insults))

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
async def roll6(ctx):
  await ctx.send(random.randint(1,6))

@bot.command()
async def roll20(ctx):
  await ctx.send(random.randint(1,20))

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data [0]['a']
  return(quote)
  
@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="discord.gg/GPQwfRF9wT"))




keep_alive()
bot.run(os.getenv('TOKEN'))
