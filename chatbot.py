import random
from os import system
#from speech import *

CONVERSING = True

memory = []
greetings = ['hola', 'hello', 'hi','hey!','Hello','Hi']
questions = ['How are you?','How are you doing?']
responses = ['Okay','I am fine']
validations = ['yes','yeah','yea','no','No','Nah','nah']
verifications = ['Are you sure?','You sure?','you sure?','sure?',"Sure?"]

while CONVERSING:
        lang = 'en-US'
        speed = .3
        
        userInput = raw_input(">>>Me: ")
        if userInput in greetings:
                random_greeting = random.choice(greetings)
                print random_greeting
                system('say %s' % (random_greeting))
                memory.append((userInput,random_greeting))
        elif userInput in questions:
                random_response = random.choice(responses)
                memory.append((userInput,random_response))
                print random_response
                system('say %s' % (random_response))
        elif userInput in verifications:
                random_response = random.choice(validations)
                memory.append((userInput,random_response))
                print random_response
                system('say %s' % (random_response))
        elif 'sure' in userInput:
                response = "Sure about what?"
                memory.append(('sure',response))
                print response
                system('say %s' % (response))
        else:
                system('say I did not understand what you said. Goodbye!')
                CONVERSING = False
                
for conversations in memory:
        print conversations

        
'''This can be extended with elif statements and eventually you will eventually have your very own slightly clever AI. Just make sure that the else statement is always at the bottom of your code'''