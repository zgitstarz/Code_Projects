import discord
from discord.ext import commands
from discord import app_commands
from jokeapi import Jokes



class BotServer(commands.Bot):
    async def on_ready(self):
        print(f"Bot Started as {self.user}")
        synced = await self.tree.sync()
        print(f"synced {len(synced)} /commands")
        print("----------\n")
    
    async def on_member_join(self, member: discord.Member):
        f1 = discord.File("./cat.jpg", filename='cat.jpg')
        ed = f"```Welcome to {member.guild.name}```"
        embed = discord.Embed(colour=discord.Colour.gold(), description=ed)
        embed.set_image(url="attachment://cat.jpg")
        await member.send(file=f1, embed=embed)




intents = discord.Intents.all()

# initializing bot with '?' prefix
bot = BotServer(command_prefix='?', intents=intents, help_command=None)

@bot.tree.command(name='addrole')
@app_commands.describe(role_name="What role should i add?")
async def addrole(interaction: discord.Interaction, role_name: str):

    print(f"Creating role {role_name}...\n")
    try:
        await interaction.guild.create_role(name=role_name)
        await interaction.response.send_message("Role creation was successfull!")
    except Exception as e:
        await interaction.response.send_message('role creation failed!\nerror: {e}')
        print(e)


@bot.tree.command(name='delrole')
@app_commands.describe(role_name='What role should i delete?')
async def delrole(interaction: discord.Interaction, role_name: str):
    role = discord.utils.get(interaction.guild.roles, name=role_name)
    try:
        await role.delete()
        await interaction.response.send_message(f"{role_name} successfully deleted")
    except Exception as e:
        await interaction.response.send_message(e)
        print(e)


@bot.tree.command(name='getjoke', description='get a random joke')
async def getjoke(interaction: discord.Interaction):
    joke_init = await Jokes()
    joke = await joke_init.get_joke()
    if joke['type'] == 'single':
        await interaction.response.send_message(str(joke['joke']))
    else:
        final_joke = f"{joke['setup']}\n{joke['delivery']}"
        try:
            await interaction.response.send_message(final_joke)
        except Exception as e:
            print(e)

# Help commands

@bot.group(invoke_without_command = True)
async def help(ctx: commands.Context):
        await ctx.send("Available help commands are:```\n\
                       help:     get help\
                       \naddrole:  add a role\
                       \ndelrole:  delete a role\
                       \nget_joke: get random joke```")

@help.command()
async def addrole(ctx: commands.Context):
    await ctx.send("```addrole <role name>```")

@help.command()
async def delrole(ctx: commands.Context):
    await ctx.send("```delrole <role name>```")

@help.command()
async def get_joke(ctx: commands.Context):
    await ctx.send("```get_joke <no arguments>```")


bot.run('TOKEN')








