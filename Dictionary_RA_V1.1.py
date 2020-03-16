import json
import difflib
from difflib import get_close_matches
from difflib import SequenceMatcher
with open("/Users/RMAda/PycharmProjects/Application_1_Dictionary/data.json","r") as dictfile:
    content = dictfile.read()
data = json.load(open("data.json"))
def eng_dict(word):
    word_lower = word.lower() #Changes word to lower case
    word_capital = word.capitalize() #Creates a variable which is a capitalised version of the word
    word_upper = word.upper()
    if word_lower in data:
        return data[word_lower] #If the lowercase word is in the dictionary, return the definition from the dictionary
    elif word_capital in data:
        return data[word_capital] #If the capitalised version of the word is in the dictionary, return the definition
    elif word_upper in data:
        return data[word_upper]
    elif len(get_close_matches(word, data.keys())) > 0: #If there is a close match to the user supplied word
        yes_or_no = input("Did you mean %s instead? Y or N: " % get_close_matches(word, data.keys())[0]) #Return a suggested word, requests user to confirm
        if yes_or_no == "Y": #If user confirms that this is the correct word
            return data[get_close_matches(word, data.keys())[0]] #Return the first match in the list
        else: return "Word not found" #Else say that the word is not found
    else:
        return "Word not found" #If there are no close matches, report "Word not found"
word = input("Enter word: ")
result = eng_dict(word) #Could just print it, but because some things have multiple definitions it is easier to read if each definition in the list is printed
if type(result) == list:
    for x in result:
        print(x)
else:
    print(result)

while True:  #This is a loop which allows users to input different words without re-loading the programme.
    message = input("Enter a word, or type \end to cancel:  ") #stores users input as a variable called message
    if message == "\end": #if user inputs \end then the program will stop
        break
    else:
        result2 = eng_dict(message) #runs the eng_dict function stored above, with the user input as the variable
        if type(result2) == list: #if the result is a list
            for y in result2: #iterate through the list
                print(y) #print each list item
        else: print(result2) #else (ie not a list) prints the result

# Sequence matcher for comparing words
#from difflib import SequenceMatcher
#SequenceMatcher(None,"rainn","rain").ratio()  #This will give the ratio of how similar these two words are
# Get close matches
# get_close_matches(word, possibilities, n=3, cutoff=0.6) #word is what we want suggestions, possibilities is a list of options, n is number of options and cutoff is the ratio (see above)
#difflib.get_close_matches("snow", ["nose", "know", "train", "car", "bike"]) returns ["know"] one close match (above 0.6 ratio)
# & C:/Users/RMAda/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/RMAda/PycharmProjects/Application_1_Dictionary/Dictionary_RA_V1.1.py
