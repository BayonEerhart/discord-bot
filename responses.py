import random
import datetime
# import logs
import pyjokes  
from wonderwords import RandomWord



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

    if p_message == "!word"[:5]:
        if p_message[6:]:
            return p_message[6:]
        r = RandomWord()
        return r.word()

        
