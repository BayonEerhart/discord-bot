import random
import datetime
import pyjokes
import re
from wonderwords import RandomWord
import random
import os
import sys
import json
import pytz
import randfacts



def handle_response(message, user_id) -> str:
    p_message = message.lower()

    if p_message == '!hello':
        return 'hey there'

    if p_message == "!joke":
        return pyjokes.get_joke()

    if re.match(r"!word (\d+)", p_message):
        number_str = re.match(r"!word (\d+)", p_message).group(1)
        number = int(number_str)
        r = RandomWord()
        sent = ""
        print(number)
        if number > 100:
            return "the number is way to big do something less than 100"
        for i in range(number):
            sent = sent + " " + r.word()
        return sent[:1999]

    if p_message == "!word":
        r = RandomWord()
        return r.word()

    if p_message == "!time":
        return "bayons time is = " + datetime.datetime.now().strftime('%I:%M:%S %p')

    if re.match(r"!time(.+)", p_message):

        with open("times.json", "r") as read_file:
            data = json.load(read_file)
        p_split = p_message.split()
        try:
            if data[p_split[1]][0] == False:
                return (datetime.datetime.now(pytz.timezone(data[p_split[1]][1])).strftime("%I:%M:%S %p"))
            if data[p_split[1]][0] == True:
                return (datetime.datetime.now(pytz.timezone(data[p_split[1]][1])).strftime('%H:%M:%S'))
        except:
            return "user does not exist"
    if p_message == "!new":
        return "!new <@user> <zone>"

    if re.match(r"!new(.+)", p_message):
        zones = ['gmt', 'cet', 'eet', 'europe/moscow', 'asia/dubai', 'asia/riyadh', 'asia/kolkata', 'asia/dhaka',
                 'asia/bangkok', 'asia/shanghai', 'asia/tokyo', 'australia/sydney', 'pacific/auckland',
                 'pacific/honolulu', 'america/anchorage', 'america/los_angeles', 'america/denver', 'america/chicago',
                 'america/new_york', 'america/argentina/buenos_aires', 'america/sao_paulo', 'europe/lisbon',
                 'atlantic/azores', 'etc/gmt+12']
        p_split = p_message.split()
        print(p_message)
        if (p_split[1][1]) != "@":
            return "just @ some one he wont bite"
        if len(p_split) == 2:
            return "you have to add a time zone;\ndont know your time zone? do !zone"
        if p_split[2] in (zones):
            with open("times.json", 'r') as file:
                data = json.load(file)

            data[p_split[1]] = [False, p_split[2]]  # for now, it's always true in till I think of a beter way

            with open("times.json", 'w') as file:
                json.dump(data, file, indent=4)
            return f"{p_split[1]} has been added!\nhis time now is: " + handle_response(("!time " + p_split[1]))
        else:
            return "you have to add a time zone;\ndont know your time zone? do !zone"

    if p_message == "!zone":
        zones = ['gmt', 'cet', 'eet', 'europe/moscow', 'asia/dubai', 'asia/riyadh', 'asia/kolkata', 'asia/dhaka',
                 'asia/bangkok', 'asia/shanghai', 'asia/tokyo', 'australia/sydney', 'pacific/auckland',
                 'pacific/honolulu', 'america/anchorage', 'america/los_angeles', 'america/denver', 'america/chicago',
                 'america/new_york', 'america/argentina/buenos_aires', 'america/sao_paulo', 'europe/lisbon',
                 'atlantic/azores', 'etc/gmt+12']
        max_len = max(len(zone) for zone in zones)
        back = ""
        for zone in zones:
            current_time = datetime.datetime.now(pytz.timezone(zone)).strftime('%H:%M:%S')
            formatted_zone = zone.ljust(max_len)
            back += f"{formatted_zone}: {current_time}\n"
        back += "\n if i forget your time zone let me know"
        return back

    if p_message == "!fact":
        return "did you know?: " + randfacts.get_fact()


    if p_message == "!commands" or p_message == "!help":
        return ("!hello                                      : says hello back\n\
!joke                                       : says a bad programming joke\n\
!word                                     : gives a random word\n\
!word <number>                : gives a random word times <number>\n\
!restart                                 : restarts the .py\n\
!time                                      : sends bayon009ke's time\n\
!time <@user>                    : sends the time of an added user\n\
!new                                       : says -> !new<@user> <zone>\n\
!new <@user> <zone>      : adds a user name + the time zone so it allows you to use !time <@user>\n\
!zone                                     : outputs all supported time zones\n")

    if p_message == "!restart" or p_message == "!kill" or p_message.split()[0] == "!new_mod":
        with open("settings.json", "r") as read_file:
            data = json.load(read_file)
        if user_id in data["mods"]:
            if p_message == "!kill":
                exit(code="bye")
            if p_message == "!restart":
                os.execl(sys.executable, sys.executable, *sys.argv)

        return "try having mod"
