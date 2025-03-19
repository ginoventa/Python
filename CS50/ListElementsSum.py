def cumSum(lista): 
    soma = int(0)
    novaLista = []
    for lista in lista: 
        soma = soma + lista
        novaLista.append(soma)
    return novaLista

lista = [1,2,3]
print(cumSum(lista))
    

#O programa busca criar uma nova lista que terá a soma dos elementos que antecedem a posição na lista original 
    #Utilizamos o método de listas append para ir adicionando elementos a essa nova lista
