import random
import datetime
# import logs
import pyjokes  
import re
from wonderwords import RandomWord
import random
import os
import sys



def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '!hello':
        return 'hey there'
 
    if p_message == "!time":
        return "bayons time is = " + datetime.datetime.now().strftime('%H:%M:%S')
    if p_message == "!logs":
        logs.minecraft_log()
        
    if p_message == "!joke":
        return pyjokes.get_joke()

    if re.match(r"!word (\d+)", p_message):
        number_str = re.match(r"!word (\d+)", p_message).group(1)
        number = int(number_str)
        r = RandomWord()
        sent = ""
        print(number)
        if number > 1000:
            return "the number is way to big do something less than 100"
        for i in range(number):
            sent = sent +  " " + r.word()
        return sent[:1999]

    if p_message == "!word":
        r = RandomWord()
        return r.word()
    if p_message == "!restart":
            os.execl(sys.executable, sys.executable, *sys.argv)
        

