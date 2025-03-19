def nested_sum(lista = []):
    somaListas = 0 
    for lista in lista: 
        somaListas = somaListas + sum(lista)
    print(somaListas)

t = [[1,2],[3],[4,5,6]]
nested_sum(t)


#O objetivo desse programa é somar listas aninhadas, ou seja, listas que estão em uma lista. Para isso fizemos
#um for que passasse pelos elementos da lista e as somasse a um contador 'somaListas'

#Função nested_sum: 
    ##Passamos a lista no for, avançando de elemento em elemento que, nesse caso, serão listas diferentes. 
    # Em cada ponto, ele irá fazer a soma de cada um dos elementos/listas e irá printar o resultado ao final 
