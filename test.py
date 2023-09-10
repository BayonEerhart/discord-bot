from wonderwords import RandomWord
import re


input_str = "!word 12"


# if match:
#     number_str = match.group(1)
    
#     number = int(number_str)
    
#     for i in range(number):
#         print(f"Iteration {i+1} of the loop.")
# else:
#     print("Input does not match the expected pattern.")


def handle_response(message) -> str:
    p_message = message.lower()
    pattern = r"!word (\d+)"
    match = re.match(pattern, p_message)
    if match:
        number_str = match.group(1)
        number = int(number_str)
        r = RandomWord()
        sent = ""
        if number > 100:
            return "the number is way to big do something less than 100"
        print(number)
        for i in range(number):
            sent = sent +  " " + r.word()
        return sent
print(handle_response(input_str))
