def is_sorted(lista): 
    lista_organizada = lista[:]
    lista_organizada.sort()

    if(lista == lista_organizada):
        print("True")
        print(lista, "/",lista_organizada)
    else:
        print("False")
        print(lista, lista_organizada)

a = [1,4,6,7,3,1,3]
b = [2,3,5,7,98]

is_sorted(a)
is_sorted(b)

#A ideia aqui é conferir se uma lista está organizada de maneira ascendente. Explicação: 

#A parte mais difícil está na linha 2:
    ##A estrturua 'lista[:]' permite que façamos uma cópia da varíavel 'lista' para 'lista_organizada', assim qualquer alteração em uma não afetará a outra. 
     ###A estrutura [:] dita que estaremos copiando do primeiro ao último elemento de tal lista 
