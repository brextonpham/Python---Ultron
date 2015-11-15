from __future__ import print_function
import httplib2
import os
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import random
import pafy
import pywapi
import string
import shlex
import requests
import wikipedia
import goslate
import datetime
from PyLyrics import *
from os import system

#Using Google Calendar API from Python QuickStart Guide
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Ultron'

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: 
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def schedule():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 5 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=5, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

CONVERSING = True

dictionary = {"hello!":[]}

print("hello! my name is Ultron! let me do things for you.")
print("below are all of my available commands, type the keyword 'key' followed by the desired command if you want me to do something, else we can just talk!")
commands = ["weather", "calculator", "lyrics", "wikipedia", "translate"]
for command in commands:
        print(">>> " + command)

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
                        print("\n")
                        print("Weather.com says: It is " + string.lower(weatherResult['current_conditions']['text']) + " and " + weatherResult['current_conditions']['temperature'] + "C now in " + zipcode + ".")
                        print("Yahoo says: It is " + string.lower(yahooResult['condition']['text']) + " and " + yahooResult['condition']['temp'] + "C now in " + zipcode + ".\n")
                elif (command == "calculator"):
                        expression = parts[2]
                        #print "\n"
                        print(eval(expression))
                        #print "\n"
                elif (command == "lyrics"):
                        splitForLyrics = shlex.split(userInput)
                        author = splitForLyrics[2]
                        song = splitForLyrics[3]
                        print(PyLyrics.getLyrics(author, song))
                elif (command == "wikipedia"):
                        splitForWikipedia = shlex.split(userInput)
                        search = splitForWikipedia[2]
                        print(wikipedia.summary(search))
                elif (command == "translate"):
                        gs = goslate.Goslate()
                        splitForTranslate = shlex.split(userInput)
                        phrase = splitForTranslate[2]
                        destination = splitForTranslate[3]
                        print(gs.translate(phrase, destination))
                elif (command == "schedule"):
                        schedule()
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




