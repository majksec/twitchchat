import socket
import datetime
import re
import optparse
import os
from colorama import Fore
from colorama import Style

parser = optparse.OptionParser("Usage: python3 chat.py -c 'channel_name'")
parser.add_option("-c", dest="channel", help="Specify twitch channel")
(options, args) = parser.parse_args()
channel = options.channel

# your twitch nickname
name = ""
# your oauth key - get it from https://twitchapps.com/tmi/
oauth = ""

#############################################################
# DO NOT MODIFY

server = "irc.chat.twitch.tv"
port = 6667

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server, port))


if channel == None:
    channel = name

sock.send(f"PASS {oauth}\n".encode("utf-8"))
sock.send(f"NICK {name}\n".encode("utf-8"))
sock.send(f"JOIN #{channel}\n".encode("utf-8"))

print("connected @ " + datetime.datetime.now().strftime("%H:%M:%S"))

while True:

    if oauth == "" or name == "":
        print("Please insert valid oauth Token and name in program!")
        break

    # reciving the message
    response = sock.recv(1024).decode()
    if len(response) != 0:
        res = "".join(response)

        # tell server that we are still listening
        if res.split()[0] == "PING":
            sock.send(f"PONG\n".encode("utf-8"))

        else:
            # set parameters
            resList = res.split()
            user = re.findall(":(.*)!.*$", resList.pop(0))
            action = resList.pop(0)
            channel = resList.pop(0)
            msg = " ".join(resList)

            # if it's channel message, show it!
            if action == "PRIVMSG":
                # format tabs for message
                if len("".join(user)) >= 24:
                    tab = ""
                elif len("".join(user)) >= 12:
                    tab = "\t"
                else:
                    tab = "\t\t"

                indent = "\t\t\t"

                # format and display message
                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                mess_final = re.sub("(.{60})", "\\1\n\t\t\t\t", msg[1:], 0, re.DOTALL)
                user_n = "".join(user)
                print(
                    f"{Fore.BLUE}{timestamp} || {Fore.CYAN}{user} {tab}: {Fore.GREEN}{mess_final}"
                )

    else:
        print("No data from server")
