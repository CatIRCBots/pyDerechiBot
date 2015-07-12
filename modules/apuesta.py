"""
apuesta.py - Se apuesta una tarea wikipédica entre el enviador y al que se le envió
---
pyDerechiBot por ElGatoSaez - pyderechibot.cf
Basado en phenny por Sean B. Palmer.
http://inamidst.com/phenny/
"""
import urllib2
import random
def apuesta(phenny, input):
    ## Tira el dado
    dado = random.randrange(0,4)
    ## Hace un ifelse para ver qué categoría le tocó a c/u 
    if dado == 0:
        categoria = 'Wikipedia:Wikificar'
    elif dado == 1:
	    categoria = 'Wikipedia:Copyedit'
    elif dado == 2:
        categoria = 'Wikipedia:Páginas_no_categorizadas'
    else:
        categoria = 'Wikipedia:Renombrar'
    ## Otro IF/ELIF que muestra mensaje
    if categoria == 'Wikipedia:Wikificar':
        piedad = 'wikificar un artículo'
    elif categoria == 'Wikipedia:Copyedit':
        piedad = 'arreglar ortografía y gramática en un artículo'
    elif categoria == 'Wikipedia:Páginas_no_categorizadas':
        piedad = 'categorizar un artículo'
    else:
        piedad = 'renombrar un artículo '
    enviador = input.nick
    apiadate = input.group(2)
    plink = 'https://es.wikipedia.org/wiki/Especial:Aleatorio_en_categor%C3%ADa/' + categoria 
    linkp = urllib2.Request(plink)
    linkr = urllib2.urlopen(linkp)
    articulo = linkr.geturl()
    articulocode = articulo.encode('utf8')
    apiadatecode = apiadate.decode('utf8')
    enviadorcode = enviador.decode('utf8')
    piedadcode = piedad.decode('utf8')
    phenny.say(enviadorcode + ' ' + 'y' ' ' + apiadatecode + ',' + ' ' + 'se han echado una apuesta por' + ' ' + piedadcode + '.')
    phenny.say('El artículo es: ' + articulocode + ' .' + ' ¡Buena suerte a ambos!') 

apuesta.commands = ['apuesta']
apuesta.priority = 'medium'