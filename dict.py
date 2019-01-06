from json import load
from difflib import get_close_matches


# use "with open" to better handle files
with open('data.json') as text:
    data = load(text)


def translate(word):
    word = word.lower()
    # instead of calling checking if the word is in the dict
    # and then searching it, simply search it with 'get'
    # if the word doesn't exist, it will return '[None]'
    found = data.get(word, [None])[0]

    if found:
        return found
    else:
        # save 'get_close_matches(word, data.keys())' in a variable
        # so you don't need to call it several times
        close_match = get_close_matches(word, data.keys())[0]
        if len(close_match) > 0:

            found = input("Is '{}' your word? [y/n] ".format(close_match))
            if found == 'y':
                return data[close_match][0]
            elif found == 'n':
                # instead of looking just the first word in 'close_match'
                # you should make a loop and keep asking the user if one
                # of the words, is their word!
                pass
            else:
                return "Please answer only with 'y' or 'n'"
        return "Sorry, word not found!"


# this 'if' makes sure that the following will only run if it's being called
# straight from the terminal/command prompt, making sure the following lines
# won't run for another module/class/script
if __name__ == '__main__':
    result = translate(input('Enter one word: '))

    # compare types with 'is' instead of '=='
    if type(result) is list:
        # right now you're only returning ONE word at a time
        # so this for is useless
        # for word in result:
        print(result)
    else:
        print(result)
