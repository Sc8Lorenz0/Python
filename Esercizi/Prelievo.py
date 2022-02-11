print ('convertitore di valuta')
print ("")
def menu():
    print ('1.  Vuoi convertire Euro in USD?')
    print ('2.  Vuoi convertire USD in Euro?')
    print ('3.  Esci dal programma')
    print ("")
menu()
i=0
menu_choice = 0
while i == 0:
    menu_choice = (int ( input ('scegli cosa vuoi fare (1-3):   ')))
    print ('Hai scelto l operazione: ', menu_choice)
    if menu_choice == 1:
        userEuro = float(input("Scrivi l'importo in Euro che vuoi convertire in dollari:  €  "))
        USD = userEuro *  1.1417
        print ("Ecco il tuo cambio: ")
        print  ("€", userEuro, " =  $ ", USD)
        print ("")
        menu()
    elif menu_choice ==2:
        userUSD = float(input("Scrivi l'importo in dollari che vuoi convertire in euro:  $  "))
        Euro = userUSD * 0.8759
        print ("Ecco il tuo cambio: ")
        print  ("$", userUSD, " =  € ", Euro)
        print ("")
        menu()
    elif menu_choice == 4:
        userSTER = (float(input("Scrivi l'importo in sterline che vuoi convertire in euro  ")))
        Sterlina = userSTER * 0.8

    elif menu_choice == 3:
        print ("grazie per aver usato questo programma!")
        break