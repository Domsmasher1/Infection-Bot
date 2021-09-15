import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands
from discord.utils import get
import os

TOKEN = os.getenv("DISCORD_TOKEN")

infectionLevel = {
  
}
voice_states = True
members = True
warcrime = "⣿⡟⠙⠛⠋⠩⠭⣉⡛⢛⠫⠭⠄⠒⠄⠄⠄⠈⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿" + f"\n⣿⡇⠄⠄⠄⠄⣠⠖⠋⣀⡤⠄⠒⠄⠄⠄⠄⠄⠄⠄⠄⠄⣈⡭⠭⠄⠄⠄⠉⠙" + f"\n⣿⡇⠄⠄⢀⣞⣡⠴⠚⠁⠄⠄⢀⠠⠄⠄⠄⠄⠄⠄⠄⠉⠄⠄⠄⠄⠄⠄⠄⠄" + f"\n⣿⡇⠄⡴⠁⡜⣵⢗⢀⠄⢠⡔⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄" + f"\n⣿⡇⡜⠄⡜⠄⠄⠄⠉⣠⠋⠠⠄⢀⡄⠄⠄⣠⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸" + f"\n⣿⠸⠄⡼⠄⠄⠄⠄⢰⠁⠄⠄⠄⠈⣀⣠⣬⣭⣛⠄⠁⠄⡄⠄⠄⠄⠄⠄⢀⣿" + f"\n⣏⠄⢀⠁⠄⠄⠄⠄⠇⢀⣠⣴⣶⣿⣿⣿⣿⣿⣿⡇⠄⠄⡇⠄⠄⠄⠄⢀⣾⣿" + f"\n⣿⣸⠈⠄⠄⠰⠾⠴⢾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⣾⢀⠁⠄⠄⠄⢠⢸⣿⣿" + f"\n⣿⣿⣆⠄⠆⠄⣦⣶⣦⣌⣿⣿⣿⣿⣷⣋⣀⣈⠙⠛⡛⠌⠄⠄⠄⠄⢸⢸⣿⣿" + f"\n⣿⣿⣿⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠈⠄⠄⠄⠄⠄⠈⢸⣿⣿" + f"\n⣿⣿⣿⠄⠄⠄⠘⣿⣿⣿⡆⢀⣈⣉⢉⣿⣿⣯⣄⡄⠄⠄⠄⠄⠄⠄⠄⠈⣿⣿" + f"\n⣿⣿⡟⡜⠄⠄⠄⠄⠙⠿⣿⣧⣽⣍⣾⣿⠿⠛⠁⠄⠄⠄⠄⠄⠄⠄⠄⠃⢿⣿" + f"\n⣿⡿⠰⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠩⠔⠒⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠘⣿" + f"\n⣿⠃⠃⠄⠄⠄⠄⠄⠄⣀⢀⠄⠄⡀⡀⢀⣤⣴⣤⣤⣀⣀⠄⠄⠄⠄⠄⠄⠁⢹ "

bot = commands.Bot(command_prefix = warcrime) #Change prefix here (default warcrime)


#Startup
#On startup puts in console that the bot is ready
@bot.event 
async def on_ready():
  print("{0.user} is ready to commit warcrimes".format(bot))
  doing = "the world burn"
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=doing))

#Nya
#Gives the user the prefix needed for the other commands 
@bot.event
async def on_message(message): 
  if message.author == bot.user:
    return 
  if message.content.startswith("nya") or message.content.startswith("Nya"): 
    await message.channel.send(warcrime)
  await bot.process_commands(message)

#Create
#Creates all the needed roles for the game to begin
@bot.command(help="This command will create all the roles needed for the bot to work.",brief="Creates needed roles.")
async def CreateRoles(ctx):
    if get(ctx.guild.roles, name="QUARANTINED BIOHAZARD"):
        await ctx.send("Role already exists")
    else:
        role = await ctx.guild.create_role(name="QUARANTINED BIOHAZARD", colour=discord.Colour(0x40a552))
        await role.edit(hoist=True)
        await ctx.send("Role created")

#Remove
#Removes the role from target user
@bot.command(help="This command will remove the role **QUARANTINED BIOHAZARD** from the target user", brief="Removes **QUARANTINED BIOHAZARD** from target user")
async def remove(ctx, user: discord.Member):
  role = get(ctx.guild.roles, name="QUARANTINED BIOHAZARD")
  try:
    await user.remove_roles(role)
    await ctx.send(f"The **QUARANTINED BIOHAZARD** role was removed from {user.mention}")  
  except:
    await ctx.send(f"The user {user.mention} did not have the role **QUARANTINED BIOHAZARD**")

#Infect
#Infects a person and gives them the role
@bot.command(help="This command will give the **QUARANTINED BIOHAZARD** role to the target user and make them infectious", brief="Infects target user")
async def infect(ctx, user: discord.Member):
  role = get(ctx.guild.roles, name="QUARANTINED BIOHAZARD")
  try:
    await user.add_roles(role)
    await ctx.send(f"{role.mention} was infected")       
  except:
     await ctx.send(f"The user {user.mention} already had the role **QUARANTINED BIOHAZARD**")

#Reset
#Removes the role and resets the game.
@bot.command(help="This command will delete the role **QUARANTINED BIOHAZARD** from all users and reset the game. You will now need to infect a new person to start up the game again.", brief="Resets the game")
async def reset(ctx):
  try:
    role = get(ctx.guild.roles, name="QUARANTINED BIOHAZARD")
    await role.delete()
  except:
    return
  role = await ctx.guild.create_role(name="QUARANTINED BIOHAZARD", colour=discord.Colour(0x40a552))
  await role.edit(hoist=True)
  await ctx.send("Bot has been reset, please infect a new user with the infect command")
    

@bot.event
async def on_member_update(before, after):
  try:
    role = get(before.guild.roles, name="QUARANTINED BIOHAZARD")
    was_hazzard = role in before.roles
    is_hazzard = role in after.roles
    if was_hazzard == is_hazzard: #No change in role
      None
    elif was_hazzard == True: #Was infected, but not now
      if after.voice.channel != None:
        infectionLevel[after.voice.channel.id] -= 2
    elif is_hazzard == True:# Wasn't infected, but is now
      print(f"initalising infection???")
      if after.voice.channel != None:
        print("1")
        infectionLevel[after.voice.channel.id] += 2
        print ("2")
        if infectionLevel[after.voice.channel.id] >= 0:
          print(f"initalising infection")
          Infected_Channel_Size = len(after.voice.channel.members)
          infectionLevel[after.voice.channel.id] = Infected_Channel_Size
          infected_channel_refrence = 0
          while Infected_Channel_Size > 0:
            print(f"starting infection")
            Membername = after.voice.member[infected_channel_refrence].id #Gets person in channel
            print(f"{Membername} has been infected")
            member = get(after.guild.members, id=Membername)
            print("1")
            await member.add_roles(role)
            print("2")
            infected_channel_refrence += 1
            Infected_Channel_Size += -1   
  except:
    print("error")
  print(infectionLevel)

#Voice events
#Manages all the voice events including infecting new people who are in voice chats  
@bot.event
async def on_voice_state_update(member, before, after):
  if before.channel == None: #if they werent in a channel before
    guild = after.channel.guild
  else: #if they left a channel
    guild = before.channel.guild
  try:
    role = get(guild.roles, name="QUARANTINED BIOHAZARD") 
    if before.channel == None:
      Before_Channel = "Empty_Channel"
      if after.channel == None:
        After_Channel = "Empty_Channel"
      else:
        After_Channel = after.channel.id
    else:
      Before_Channel = before.channel.id
      if after.channel == None:
        After_Channel = "Empty_Channel"
      else:
        After_Channel = after.channel.id
    infectionLevel.setdefault(Before_Channel, 0)
    infectionLevel.setdefault(After_Channel, 0)
    if role in member.roles == True:
      infectionLevel[Before_Channel] += -1
      infectionLevel[After_Channel] += 1
      if After_Channel != "Empty_Channel":
        if infectionLevel[After_Channel] >= 0:
          Infected_Channel_Size = len(after.channel.members)
          infectionLevel[After_Channel] = Infected_Channel_Size
          infected_channel_refrence = 0
          while Infected_Channel_Size > 0:
            await after.voice.channel.members[infected_channel_refrence].add_roles(role)
            infected_channel_refrence += 1
            Infected_Channel_Size += -1
    else:
      infectionLevel[Before_Channel] += 1
      infectionLevel[After_Channel] += -1 
      if Before_Channel != "Empty_Channel": 
        if infectionLevel[Before_Channel] >= 0:
          Infected_Channel_Size = len(before.channel.members)
          infectionLevel[Before_Channel] = Infected_Channel_Size
          infected_channel_refrence = 0
          while Infected_Channel_Size > 0:
            await before.channel.members[infected_channel_refrence].add_roles(role)
            infected_channel_refrence += 1
            Infected_Channel_Size += -1
      if After_Channel != "Empty_Channel":
        if infectionLevel[After_Channel] >= 0:
          Infected_Channel_Size = len(after.channel.members)
          infectionLevel[After_Channel] = Infected_Channel_Size
          infected_channel_refrence = 0
          while Infected_Channel_Size > 0:
            await after.channel.members[infected_channel_refrence].add_roles(role)
            infected_channel_refrence += 1
            Infected_Channel_Size += -1
  except:
    None
  print(infectionLevel)

server.server()
bot.run(TOKEN)

