'''
bibliopaliza.py - Explica si gana un biblio o es palizón. ¡Gózenlo!
Con ayuda de dlcastc, político que milita en el partido de la Plaza Roja, Rusia.
---
pyDerechiBot por ElGatoSaez
basado en phenny por Sean B. Palmer
pyderechibot.cf - @pyDerechiBot
'''
def bibliopaliza(phenny, input):
    votosafavor = input.group(2)
    votosencontra = input.group(3)
    if int(votosencontra) * 4 > int(votosafavor):
        phenny.say("El usuario, con " + votosafavor + " votos a favor, y " + votosencontra + " votos en contra, no es electo bibliotecario")
    elif int(votosencontra) * 4 == int(votosafavor):
        phenny.say("El usuario, con " + votosafavor + " votos a favor, y " + votosencontra + u' votos en contra, ¡llevaría un perfecto empate!')
    else:
        phenny.say("El usuario, con " + votosafavor + " votos a favor, y " + votosencontra + u' votos en contra, sería electo bibliotecario. ¡Habemus biblio!')
bibliopaliza.rule = (['chequeocab'], r'(\d+) (\d+)')
bibliopaliza.priority = 'low'