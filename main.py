
import discord
import os
from discord.ext import commands
import pizzapy

num1 = False
address1 = ""
name1 = ""
credit1 = ""
Bot = commands.Bot(command_prefix='$')
client = discord.Client
store = address1.closest_store()
menu = store.get_menu

@Bot.command()
async def menu(ctx , item ):
  ki == menu.search(item)
  await ctx.send(ki)

  
@Bot.command()
async def foo(ctx, name, address , credit):
  address1 == address 
  name1 == name
  credit1 == credit
  num1 == True  

@Bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

Bot.run(os.getenv('TOKEN'))
client.run (os.getenv("TOKEN"))