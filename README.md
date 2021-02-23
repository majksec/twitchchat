# twitchchat
Realtime terminal twitch chat project.

# Contributors:
@shkabo | https://github.com/shkabo

# MUST CHANGE:
You MUST change 2 things in the script:

Line 13

name = '<your_twitch_nickname'

line 15

oauth = '<your_oauth_token>' #Token can be found here: https://twitchapps.com/tmi/

# To join specific channel use:
python3 chat.py -c <channel_name>

*In order this to work you MUST specify your nickname as explained above*
# To join your channel chat run program without arguments:
python3 chat.py

# REQUIREMENTS:
socket

datetime

re

optparse

os
