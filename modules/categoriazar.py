"""
categoriazar.py - Da un artículo o subcategoría de una categoría en Wikipedia
---
pyDerechiBot por ElGatoSaez - pyderechibot.cf
Basado en phenny por Sean B. Palmer.
http://inamidst.com/phenny/
"""
import urllib2
def categoriazar(phenny, input):
    categoria = input.group(2)
    codecategoria = categoria.encode('utf8')
    plink = 'https://es.wikipedia.org/wiki/Especial:Aleatorio_en_categor%C3%ADa/' + codecategoria
    linkp = urllib2.Request(plink)
    linkr = urllib2.urlopen(linkp)
    articulo = linkr.geturl()
    thearticle = articulo.decode('utf8')
    phenny.say(thearticle)
categoriazar.commands = ['categoriazar']
categoriazar.priority = 'medium'