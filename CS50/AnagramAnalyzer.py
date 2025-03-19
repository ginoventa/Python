
def is_anagram(palavra1,palavra2):
    if len(palavra2) == len(palavra1):
        lista_palavra1 = list(palavra1)
        lista_palavra2 = list(palavra2)

        for i in palavra1:
            if i in lista_palavra2:
                print(lista_palavra1, lista_palavra2)
                lista_palavra2.remove(i)
                print(lista_palavra1, lista_palavra2)
       
        if lista_palavra2 == []:
            print("True")
        else:
            print("False")



palavra1 = 'Giovanna'
palavra2 = 'annaGiov'

is_anagram(palavra1,palavra2)


#Esse programa busca saber se duas palavras distintas são capazes de escreverem uma a outra. Para isso, precisamos saber se ambas as palavras possuem mesmo tamanho, e 
#se possuem a mesma quantidade de letras. A cada letra igual encontrada essa letra é retirada da outra palavra, assim conseguimos descobrir se eles possuem o mesmo numero das mesmas letras
#Resultando em 0, podemos afirmar que são anagramas

# A estrutura ---- in ---- confere se algo está em outro algo e ----- is -----

