import random
from os import system

CONVERSING = True

dictionary = {"hello!":[]}

bot = "hello!"
while CONVERSING:
        print("B: " + bot)
        system('say %s' % (bot))
        userInput = raw_input("H: ")
        dictionary[bot].append(userInput.lower())
        if (not dictionary.has_key(userInput)):
                dictionary.update({userInput:[]})
                bot = userInput
        else:
                listChoice = dictionary[userInput]
                bot = random.choice(listChoice)



