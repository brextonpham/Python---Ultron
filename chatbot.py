import random
import pafy
import pywapi
import string
import shlex
from PyLyrics import *
from os import system

CONVERSING = True

dictionary = {"hello!":[]}

print "hello! my name is Ultron! let me do things for you."
print "below are all of my available commands, type the keyword 'key' followed by the desired command if you want me to do something, else we can just talk!"
commands = ["weather", "calculator", "lyrics"]
for command in commands:
        print ">>> " + command

bot = "hello!"
while CONVERSING:
        print("B: " + bot)
        system('say %s' % (bot))
        userInput = raw_input("H: ")

        parts = userInput.split(' ')
        checkForKeyword = parts[0]

        if (checkForKeyword == 'key'):
                command = parts[1]
                if (command == "weather"):
                        zipcode = parts[2]
                        weatherResult = pywapi.get_weather_from_weather_com(zipcode)
                        yahooResult = pywapi.get_weather_from_yahoo(zipcode)
                        print "\n"
                        print "Weather.com says: It is " + string.lower(weatherResult['current_conditions']['text']) + " and " + weatherResult['current_conditions']['temperature'] + "C now in " + zipcode + "."
                        print "Yahoo says: It is " + string.lower(yahooResult['condition']['text']) + " and " + yahooResult['condition']['temp'] + "C now in " + zipcode + ".\n"
                elif (command == "calculator"):
                        expression = parts[2]
                        #print "\n"
                        print eval(expression)
                        #print "\n"
                elif (command == "lyrics"):
                        splitForLyrics = shlex.split(userInput)
                        author = splitForLyrics[2]
                        song = splitForLyrics[3]
                        print(PyLyrics.getLyrics(author, song))
                continue
        elif (checkForKeyword == "" or checkForKeyword == " "):
                CONVERSING = False
        dictionary[bot].append(userInput.lower())
        if (not dictionary.has_key(userInput)):
                dictionary.update({userInput:[]})
                bot = userInput
        else:
                listChoice = dictionary[userInput]
                bot = random.choice(listChoice)




