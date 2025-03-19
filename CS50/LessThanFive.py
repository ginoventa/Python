amostra = [1,2,3,4,5,6,7,8,9,10]

for i in amostra[:]: 
    if i % 2 : 
        amostra.remove(i)

print(amostra)


#Linha 3/Estrutura for: temos uma estrutra de loop que passa pelos numeros da amostra, e não pela interação padrão de 0-9
    ##Neste caso, se o elemento em questão for divisível por 2 ele será removido por meio de amostra.remove(i), que busca o elemento de mesmo valor do () e retira-o da lista
    ### Nesse caso, a condicional 'i in amostra[:]' cria uma cópia da lista original e vai iterando ao longo dela 

#Nova ideia: vimos que essa lista diminui simultaneamente com a retirada de seus elementos, de maneira que usar o for como em C não funcionaria

amostras = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(amostras) - 1, -1, -1): 
    if amostras[i] % 2 : 
        amostras.pop(i)

print(amostras)

#Aqui temos uma nova maneira de pensar, ao invés de irmos de frente para trás iremos de trás para frente
    ##A estrutura for começa no 9, e vai iterando -1 até chegar ao espaço 0. Dessa maneira, conseguimos passar por todos os números mesmo com a lista diminuindo. 
    ###Isso é muito bom, porque aqui fazemos a retirada por posição com o 'amostras.pop(i)'
