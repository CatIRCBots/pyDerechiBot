#!/usr/bin/env python
"""
ping.py - Phenny Ping Module
Author: Sean B. Palmer, inamidst.com
About: http://inamidst.com/phenny/
---
pyDerechiBot por ElGatoSaez - pyderechibot.cf
Basado en phenny por Sean B. Palmer.
http://inamidst.com/phenny/
 - ping y pong lo codeé yo
"""

import random

def hello(phenny, input): 
   greeting = random.choice(('Hi', 'Hey', 'Hello', 'Hola', 'Buenas'))
   punctuation = random.choice(('', '!'))
   phenny.say(greeting + ' ' + input.nick + punctuation)
hello.rule = r'(?i)(hi|hello|hey|hola|buenas) $nickname[ \t]*$'

def interjection(phenny, input): 
   phenny.say(input.nick + '!')
interjection.rule = r'$nickname!'
interjection.priority = 'high'
interjection.thread = False

def ping(phenny, input):
    phenny.say(input.nick +',' + ' pong!')
ping.commands = ['ping']
ping.priority = 'medium'

def pong(phenny, input):
	phenny.say(input.nick +',' + ' ping!')
pong.commands = ['pong']
pong.priority = 'medium'

if __name__ == '__main__': 
   print __doc__.strip()
