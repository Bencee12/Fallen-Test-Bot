import discord 
from discord.ext import commands 

client = commands.Bot(command_prefix="f.")

@client.event
async def on_ready():
    print(f"-----\nBejelentkezve: {client.user.name} : {client.user.id}\n-----\nPrefix: -\n-----")
    # Another way to use variables in strings
    print("-----\nBejelentkezve: {} : {}\n-----\nPrefix:: -\n-----".format(client.user.name, client.user.id))
    await client.change_presence(activity=discord.Game(name=f"{client.user.name}.\nSegítség Kérésért: -help")) # This changes the clients 'activity'


@client.command()
async def szia(ctx):

    await ctx.send(f'Szia {"{}".format(ctx.message.author.mention)}!')


client.run('NzIwMTc2NzQzODU1NDIzNDg4.XuCK2w.liDxZX0h2EQldBj3n58-QMmqNEQ')

client.remove_command('help')

@client.command()
async def help(ctx):
    await ctx.send("Parancsok: f.szia")