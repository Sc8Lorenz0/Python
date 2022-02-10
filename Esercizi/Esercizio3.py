l_array  = int (input ("Inserisci il numero n degli elememnti della lista: "))
lista = list(range (1, l_array  +1, 1))
print ("")
for x in range(l_array):
    print (lista[x],x)
    print ("")
    x +=x