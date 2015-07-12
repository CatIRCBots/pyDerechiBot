'''
El código más lento del mundo, denominado así debido a las complicaciones y lentitud
de codearlo, finalmente, son {{CODELINES}} líneas de código. Y siguen avanzando.
@ElGatoSaez - pyderechibot.cf
Basado en Phenny por Sean B. Palmer
inamistd.com/phenny
'''
import twitter
import urllib2
import json
import pickle
def timeline(phenny, input):
    user = input.group(2)
    paralaapi = '@' + user
    api = twitter.Api(consumer_key='ea4kkFgHkartFAh6MSwhoEQl6',consumer_secret='8aFjAW8LvCnVzaUAPl5xfOJ4BXVDGD048D2EeNFtS4tkzBgtA4',access_token_key='149726972-ZrnsxJnoBfaEzy8yeX5dQbc4M8lwTPrJEZwKDcV8',access_token_secret='qpMal361flort46lvcNdZ2GRekeA4qQ61bpQK1qdw9qOj')
    statuses = api.GetUserTimeline(screen_name=user, count=1)
    ad = [s.text for s in statuses]
    prnt = ad[0]
    dontdonothing = 0
    if prnt.startswith("RT"):
        rtif = "[RT]"
    else:
        dontdonothing = 1
# Este código es para probar en PowerShell, por favor, omitir.
    #if dontdonothing == 0:
    #print rtif + prnt
    #else:
#print prnt
    adc1 = prnt.replace("RT", "")
# print rtif + adc1
    user = adc1.split(':', 1)
    useru = user[0]
#print useru
    userr = useru.replace(" ", "")
    userf = "[" + userr + "]"
#print userf
# Este código también es para probar en PowerShell, omitir por favor.
#if dontdonothing == 1:
    #print prnt 
#else:
    #print rtif + userf + prnt
    if dontdonothing == 1:
        ftweet = "[ " + prnt + " ]"
    else:
        ftweet = prnt.split(': ', 1)[1]
## The final countdown
#print rtif
#print userf
#print ftweet
    if dontdonothing == 1:
        phenny.say(ftweet)
    else:
        phenny.say(rtif + " " + userf + " " + "[ " + ftweet + " ]")
timeline.commands = ['timeline']
timeline.priority = 'high'