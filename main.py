import discord
import os
import requests
import json
import random
from replit import db
from discord.ext import commands
from keep_alive import keep_alive

client = discord.Client()

help_message = "Commands: %inspire, %help, %insult, %smokingoose, %coinflip, %invite, %hyperwolf, %rndltr, %rolldice"
pings = ["@"]
weebs_bad = ["weeb", "Weeb"]
weebs_bad_response = "Ew, weebs."
pinged = "Someone was pinged here, or the @ symbol was used."
flip_a_coin = ["Heads", "Tails"]
noob = ["noob", "nub", "noooob", "Noob", "Nub", "Noooob"]
noob_responses = ["You are noob", "You are big noob"]
insults = ["fuck you", "You're the type of person to like the warm side of the pillow.", "You're the human equivalent of a participation award.", "You’re the definition of a birth defect.", "You have small pp."]
smokin_goose = "Smokin' Goose bot created on July 12th 2021. Created by Hyperwolf#2525."
h_t = ["hello there", "Hello there", "Hello There", "hellothere"]
g_k = "General Kenobi!"
invite_link = "Invite link currently unavaliable."
hyperwolf_desc = "Creator of the bot Smokin' Goose."
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
dice_d6 = ["1","2","3","4","5","6"]


if "responding" not in db.keys():
  db["responding"] = True
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data [0]['a']
  return(quote)
  
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('%inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in pings):
    await message.channel.send(pinged)

  if any(word in msg for word in weebs_bad):
      await message.channel.send(weebs_bad_response)

  if any(word in msg for word in noob):
    await message.channel.send(random.choice(noob_responses))

  if msg.startswith('%help'):
    await message.channel.send(help_message)

  if msg.startswith('%coinflip'):
    await message.channel.send(random.choice(flip_a_coin))

  if msg.startswith('%insult'):
    await message.channel.send(random.choice(insults))

  if msg.startswith('%smokingoose'):
    await message.channel.send(smokin_goose)

  if msg.startswith('%invite'):
    await message.channel.send(invite_link)

  if msg.startswith('%hyperwolf'):
    await message.channel.send(hyperwolf_desc)
  
  if any(word in msg for word in h_t):
    await message.channel.send(g_k)

  if msg.startswith('%rndltr'):
    await message.channel.send(random.choice(letters))

  if msg.startswith('%rolldice'):
    await message.channel.send(random.choice(dice_d6))

keep_alive()
client.run(os.getenv('TOKEN'))