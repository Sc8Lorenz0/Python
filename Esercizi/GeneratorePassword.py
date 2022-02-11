#Generatore password: da input indicare la grandezza della passwd da generare. Si devono
#utilizzare: maiuscole, minuscole, numeri e simboli.

import random 
import re

def genera_passcode(numero_caratteri):
    caratteri = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                 '!£$%#&=?0123456789')
    while True:
        passcode = ''
        for i in range (0, int (numero_caratteri)):
            passcode += random.choice(caratteri)
        if valida_passcode(passcode):
            break
        else:
            print ('{}:non valida come passcode, la scarto....' .format(passcode))
    return passcode 

def valida_passcode (passcode):
    condizione_validità = ('^.(?=.{'+str(len(passcode))+',})(?=.\d)(?=.[a-z])'
                        '(?=.[A-Z])(?=.[!£$%&#=?]).$')
    return re.findall(condizione_validità, passcode)

if __name__ == '__main__':
    numero_caratteri = input ("Inserisci la lunghezza del passcode per favore: ")
    passcode_generata = genera_passcode (numero_caratteri)
    print ()
    print ("Password generata: {}".format(passcode_generata ))