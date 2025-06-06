# pyjokes is external module which is installed just by using pip install command and
# imported in pyhon using import

import pyjokes
joke = pyjokes.get_joke()
print(joke)

import pyttsx3
engine = pyttsx3.init()
engine.say("Hey, This code is just copy Pasted by the writer to understand external modules")
engine.runAndWait()

#  Useful Built-ins for Exploration

print(dir(pyttsx3)) # list attributes/functions in a module.

help(pyjokes) #detailed docstring and help.
# module.__doc__ — module documentation string.