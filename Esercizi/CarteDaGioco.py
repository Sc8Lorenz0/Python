from random import *

seed()
semi = ["Quadri", "Fiori", "Picche", "Cuori"]
valori = ["Asso", 2, 3, 4, 5, 6, 7, "Fante", "Cavallo", "Re"]
carte = []
while True:
    risp = input("Premi E per uscire, Invio per estrarre una carta ")
    print("_._._._._._._._._._._._")
    if risp == "E":
        break
    if len(carte) == 0:
        carte = list(range(40))
        shuffle(carte)
        print("Attendi! Sto mescolando il mazzo")
        print("-.-.-.-.-.-.-.-.-.-.-.-.-")
        print("_._._._._._._._._._._._._")
    c = carte.pop()             
    s = c // 10                 
    val = c % 10              
    print("")  
    print(valori[val], "di", semi[s])
    print("")
print("Grazie per aver giocato.")