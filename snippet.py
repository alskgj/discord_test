# from
# https://realpython.com/how-to-make-a-discord-bot-python/

# import the module
import discord


# initialize a discord client
client = discord.Client()


@client.event
async def on_ready():
    """Called when the client is done preparing the data received from Discord.
    Usually after login is successful."""
    print("Bot is ready!")


@client.event
async def on_message(message):
    """Fired when a message is sent?"""

    if str(message.author) == "nen#0496":
        print("gin has written something")
        await message.channel.send("wow akashi, what a story")
    elif str(message.author) == "Akashiro_Krax#8700":
        await message.channel.send("really not gin")
    else:
        print("that was", message.author)

# run the discord bot
client.run(token)
