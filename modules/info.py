#!/usr/bin/env python
"""
info.py - Phenny Information Module
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.
http://inamidst.com/phenny/
"""

def doc(phenny, input): 
   """Shows a command's documentation, and possibly an example."""
   name = input.group(1)
   name = name.lower()

   if phenny.doc.has_key(name): 
      phenny.reply(phenny.doc[name][0])
      if phenny.doc[name][1]: 
         phenny.say('e.g. ' + phenny.doc[name][1])
doc.rule = ('$nick', '(?i)(?:help|doc) +([A-Za-z]+)(?:\?+)?$')
doc.example = '$nickname: doc tell?'
doc.priority = 'low'

def commands(phenny, input): 
   phenny.say(u'Te enviaré un MP con todos mis comandos')
   phenny.msg(input.nick, "Lista de comandos: selfie, search, apuesta, wuweather, seen, beats, t, o, duck, ddg, pong, ayuda, quit, chequeocab, stats, val, ngc, suggest, py, ping, pinericosas, gcs, comp, snippet, calc, yi, invite, wa, timeline, ogc, oldgc, title, part, wik, presente, join, bing, bytes, weather, hello, in, u, partido, categoriazar, assimvocemata, at")
commands.commands = ['comandos']
commands.priority = 'medium'

def ayuda(phenny, input): 
   response = (
      'Hola, Soy un bot. Diga ".comandos" para conseguir una lista ' + 
      'de mis comandos, o visite http://inamidst.com/phenny/ para mas ' + 
      'detalles generales. Soy administrado por %s.'
   ) % phenny.config.owner
   phenny.reply(response)
ayuda.commands = ['ayuda']
ayuda.priority = 'low'

def stats(phenny, input): 
   """Show information on command usage patterns."""
   commands = {}
   users = {}
   channels = {}

   ignore = set(['f_note', 'startup', 'message', 'noteuri'])
   for (name, user), count in phenny.stats.items(): 
      if name in ignore: continue
      if not user: continue

      if not user.startswith('#'): 
         try: users[user] += count
         except KeyError: users[user] = count
      else: 
         try: commands[name] += count
         except KeyError: commands[name] = count

         try: channels[user] += count
         except KeyError: channels[user] = count

   comrank = sorted([(b, a) for (a, b) in commands.iteritems()], reverse=True)
   userank = sorted([(b, a) for (a, b) in users.iteritems()], reverse=True)
   charank = sorted([(b, a) for (a, b) in channels.iteritems()], reverse=True)

   # most heavily used commands
   creply = 'most used commands: '
   for count, command in comrank[:10]: 
      creply += '%s (%s), ' % (command, count)
   phenny.say(creply.rstrip(', '))

   # most heavy users
   reply = 'power users: '
   for count, user in userank[:10]: 
      reply += '%s (%s), ' % (user, count)
   phenny.say(reply.rstrip(', '))

   # most heavy channels
   chreply = 'power channels: '
   for count, channel in charank[:3]: 
      chreply += '%s (%s), ' % (channel, count)
   phenny.say(chreply.rstrip(', '))
stats.commands = ['stats']
stats.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
