'''
pinericosas.py - Da una frase graciosa de Piñera
Partido por la mitad con UAwiki xD
---
pyDerechiBot por ElGatoSaez
basado en phenny por Sean B. Palmer
pyderechibot.cf - @pyDerechiBot
'''
import random
def pinericosas(phenny, input):
    global  pineriNumber
    pineriNumber = random.randrange(0,11)
    if pineriNumber == 0:
         phenny.say("Por el terremoto, que remeció la tierra bajo nuestros pies. Y por el marepoto, que sacudió nuestras costas.")
    elif pineriNumber == 1:
         phenny.say("Iquique ganó la Copa América y va a jugar la Sudamericana")
    elif pineriNumber == 2:
         phenny.say("Si usted maneja, no conduce")
    elif pineriNumber == 3:
         phenny.say("Durante nuestro Gobierno, vamos a entregar cinco nuevos ‘tiatros’ regionales en Iquique, La Serena, ‘Rancuagua’, Concepción y Punta Arenas")
    elif pineriNumber == 4: 
         phenny.say("A las miembros y ‘miembras’ de la Comisión Mujer, Trabajo y Maternidad")
    elif pineriNumber == 5:
         phenny.say("Estaremos viajando no solamente entre continentes, sino que a esa altura todos los planetas de nuestra ‘galáctea´")
    elif pineriNumber == 6:
         phenny.say("No da lo mismo que una mujer afectada de cáncer de mamos se intervenga precozmente")
    elif pineriNumber == 7:
         phenny.say("Alerta de ‘tusunami´")
    elif pineriNumber == 8:
         phenny.say("Hemos logrado gran solución para proteger santuario de naturaleza punta choros, isla damas y ‘gabiota´ (A través de Twitter)")
    elif pineriNumber == 9:
         phenny.say("En 20 días hemos avanzado más que otros en 20 años")
    else:
         phenny.say("Que nos subamos, como decía Einstein, sobre los hombros de gigantes")
   
pinericosas.commands = ['pinericosas']
pinericosas.priority = 'medium'