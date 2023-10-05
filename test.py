import quotes_generator




def test(p_message):
    if p_message == "!quete":
        quote = quotes_generator.motivational_quotes()
        print(quote)



    return 0



user_input = "!quete"

print(test(user_input))
