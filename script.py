# Credits to multiple discord leaver projects on github for the idea
# https://github.com/Ethical7919/Discord-Group-Leaver
# https://github.com/Otttter/Group-Leaver
# https://github.com/LarpBeta/Discord-Group-Chat-Leaver
# https://github.com/6uv/Mass-discord-group-leaver


import discord
import pyperclip

client = discord.Client()

@client.event
async def on_connect():
    print(f"Connected {client.user.name}") # So the user knows the script is working properly.
    while True:
        groupChannels = filter(lambda channel: isinstance(channel, discord.GroupChannel), client.private_channels)
        for channel in groupChannels:
            try:
                print(channel) # Showcase the group that we left
                await channel.leave() # Comment this line out if you wanna test without making any changes
            except Exception as e:
                print(e)


str = """window.webpackChunkdiscord_app.push([
  [Math.random()],
  {},
  req => {
    if (!req.c) return;
    for (const m of Object.keys(req.c)
      .map(x => req.c[x].exports)
      .filter(x => x)) {
      if (m.default && m.default.getToken !== undefined) {
        return copy(m.default.getToken());
      }
      if (m.getToken !== undefined) {
        return copy(m.getToken());
      }
    }
  },
]);""" # Javascript to be pasted into the dev console of discord to force it to give us the user token

pyperclip.copy(str) # Copy the string to the clipboard
print("Open discord devtools, and paste the code there, press enter, afterwards come back here and paste, then press enter.")

token = input("User Token: ")
client.run(token, bot=False, reconnect=True)