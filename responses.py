import random
import datetime

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '!hello':
        return 'hey there'
    
    if p_message == "!roll":
        return str(random.randint(0,100))

    if p_message == "!help":
        return "figer it out buddy"
    
    if p_message == "!did bayon steal my info":
        return "not yet"
    
    if p_message == "!is mlaxx bald":
        return "yes sir"

    if p_message == "!ok":
        return ":ok_hand:"
    if p_message == "!what time is it for bayon?":
        return "bayons time is = " + datetime.datetime.now().strftime('%H:%M:%S')