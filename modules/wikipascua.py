"""
wikipascua.py - Da una tarea wikipédica
---
pyDerechiBot por ElGatoSaez - pyderechibot.cf
Basado en phenny por Sean B. Palmer.
http://inamidst.com/phenny/
"""
import urllib2
import random
def presente(phenny, input):
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
        piedad = 'te ha enviado un artículo para que wikifiques'
    elif categoria == 'Wikipedia:Copyedit':
        piedad = 'te ha enviado un artículo para que arregles ortografía y gramática'
    elif categoria == 'Wikipedia:Páginas_no_categorizadas':
        piedad = 'te ha enviado un artículo para que categorices'
    else:
        piedad = 'te ha enviado un artículo para que renombres'
    enviador = input.nick
    apiadate = input.group(2)
    if not apiadate:
        abc = 'xyz'
    else:
        apiadatecode = apiadate.encode('utf8')
    plink = 'https://es.wikipedia.org/wiki/Especial:Aleatorio_en_categor%C3%ADa/' + categoria 
    linkp = urllib2.Request(plink)
    linkr = urllib2.urlopen(linkp)
    articulo = linkr.geturl()
    articulocode = articulo.decode('utf8')
    enviadorcode = enviador.decode('utf8')
    alonepiedad = piedad[35:]
    codealonepiedad = alonepiedad.decode('utf8')
    piedadcode = piedad.decode('utf8')
    if not apiadate:
        phenny.say(u'Te ha tocado un artículo para que' + codealonepiedad + ':' + ' ' + articulocode)
    else:
        phenny.say(apiadatecode + ',' + ' ' + enviadorcode + ' ' + piedadcode + ':' + ' ' + articulocode)

presente.commands = ['presente']
presente.priority = 'medium'