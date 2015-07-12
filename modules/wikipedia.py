"""
Escrito desde cero.
Nuevo wikipedia.py por ElGatoSaez.
---
pyDerechiBot por ElGatoSaez - pyderechibot.cf
Basado en phenny por Sean B. Palmer.
http://inamidst.com/phenny/
"""
import json
import urllib2
# ---
def buscapedia(phenny, input):
    loquedice = input.group(2)
    loquediceSinESPACIADO = loquedice.replace(" ", "%20")
    linkParaABRIR = "https://es.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=" + loquediceSinESPACIADO + "&utf8"
    link = urllib2.urlopen(linkParaABRIR)
    lealo = json.loads(link.read())
    # --- Acá llega ayuda para conseguir el value
    for page in lealo['query']['pages'].values():
        elNumero = page['pageid'] 
    numeroparajson = str(elNumero)
    pequenoextracto = lealo['query']['pages'][numeroparajson]['extract']
    link = "http://es.wikipedia.org/wiki/" + loquediceSinESPACIADO
    phenny.say(pequenoextracto)
    phenny.say(link)
buscapedia.commands = ['wik']
buscapedia.priority = 'high'
