import random
import pafy
import pywapi
import string
from os import system

CONVERSING = True

dictionary = {"hello!":[]}
#weather_com_result = pywapi.get_weather_from_weather_com('10001')
#print "Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in New York.\n\n"

print "hello! my name is Ultron! let me do things for you."
print "below are all of my available commands, type the keyword 'key' followed by the desired command if you want me to do something, else we can just talk!"
commands = ["weather"]
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
                continue
        dictionary[bot].append(userInput.lower())
        if (not dictionary.has_key(userInput)):
                dictionary.update({userInput:[]})
                bot = userInput
        else:
                listChoice = dictionary[userInput]
                bot = random.choice(listChoice)


