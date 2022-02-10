print ("Benvenuto all'esercizio sulle tariffe dei viaggi.")
print ("")
biglietto = float(input ("Inserisci il costo del biglietto: "))
print ("Seleziona una tariffa")
print ("")
tariffa = input("Inserisci tariffa: ")
print ("")
sconto1 = biglietto - (biglietto * 0.1)
sconto2 = biglietto - (biglietto * 0.15)
sconto3 = biglietto - (biglietto * 0.25)
if tariffa == 'p':
    print ("Hai diritto ad uno sconto del 10%")
    print ("")
    print ("Il truo biglietto verrà a costare: ",sconto1)
elif tariffa == 's':
    print ("Hai diritto ad uno sconto del 15%")
    print ("")
    print ("Il truo biglietto verrà a costare: ", sconto2)
elif tariffa == 'd':
    print ("Hai diritto ad uno sconto del 25%")
    print ("")
    print ("Il truo biglietto verrà a costare: ", sconto3)
elif tariffa != 'p' 's' 'd':
    print ("Il biglietto viene: ",biglietto)