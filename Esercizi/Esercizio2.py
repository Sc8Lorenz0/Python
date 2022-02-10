numero_caratteri  = int (input ("Inserisci il numero n degli elememnti della lista: "))
lista = list(range (1, numero_caratteri  +1, 1))
for i in range (numero_caratteri ):
    if lista[i]%5==0:
        divisibile = lista[i]
        print (divisibile, "È un multiplo di 5")
        print(lista[i], "è nella posizione n: ", i)
        print (" ")
    i+=i