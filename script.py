# Credits to multiple discord leaver projects on github for the idea
# https://github.com/Ethical7919/Discord-Group-Leaver
# https://github.com/Otttter/Group-Leaver
# https://github.com/LarpBeta/Discord-Group-Chat-Leaver
# https://github.com/6uv/Mass-discord-group-leaver


import discord
import sys

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


def smrdimMeni():
    valid = {"1": 1, "2": 2, "3": 3}
    while True:
        # sys.stdout.write(question + prompt)
        sys.stdout.write(f"Input a number from the following list below:\n")
        sys.stdout.write(f"1. Groups\n")
        sys.stdout.write(f"2. Servers\n")
        # sys.stdout.write(f"3. Friends\n")
        choice = input().lower()

        if choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please write out number\n")


def menuSwitch(number:int):
    match number:
        case 1:
            return filter(lambda channel: isinstance(channel, discord.GroupChannel), client.private_channels)
        case 2:
            return filter(lambda channel: isinstance(channel, discord.Guild), client.guilds)
        # case 3:
            return filter(lambda channel: isinstance(channel, discord.User), client.users)

        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            return filter(lambda channel: isinstance(channel, discord.GroupChannel), client.private_channels)

client = discord.Client()


cbool = True
@client.event
async def on_connect():
    global cbool
    print(f"Connected {client.user.name}") # So the user knows the script is working properly.
    while cbool:
        results = menuSwitch(smrdimMeni())
        for channel in results:
            try:
                # print(channel) # Showcase the group that we left
                if(query_yes_no(f"Leave {channel}","no")):
                    await channel.leave() # Comment this line out if you wanna test without making any changes
            except Exception as e:
                print(e)
        cbool = False  
        break
    sys.exit("Finished")
    


token = ""
client.run(token, bot=False, reconnect=True)
