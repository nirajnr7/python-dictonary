import json
from difflib import get_close_matches

data=json.load(open('data.json'))

def translate(string):
    string=string.lower()
    if string in data:
        return data[string][0]
    elif len(get_close_matches(string,data.keys()))>0:
        
        yn=input('is this  %s your word ? y/n '%get_close_matches(string,data.keys())[0])
        if yn=='y':
            return data[get_close_matches(string,data.keys())[0]]
        elif yn=='n':
            return "sorry no word found!." 
        else:
            return "we didn't understand your entry"

    else:
        return "sorry no word found! ."
string=input('enter word: ')
result=translate(string)

if type(result)==list:
    for i in result:
        print(i)
else:
    print(result)