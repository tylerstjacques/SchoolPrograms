abbr_dict = {"B4": "before", "BF": "boyfriend", "LOL": "Laugh Out Loud",
             "OMG": "Oh, my Gosh!"}
user_input = input('Enter an abbreviation')
if user_input in abbr_dict:
    print(abbr_dict[user_input])
else:
    input = input('What does this abbreviation mean?')
    abbr_dict[user_input] = input

print(abbr_dict)

