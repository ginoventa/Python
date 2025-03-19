tamanhoLista = int(input("Tamanho da lista: "))

lista = []

for i in range(0,tamanhoLista):
    lista.append(int(input(f"Elemento {i}: ")))

print(lista)

for i in range(0,tamanhoLista-1):
    if (lista[i]%2):     
       lista.pop(i)

print(lista)


#Esse programa tem o objetivo de retornar apenas os elementos pares de uma lista de números 

#Explicação: 

#Linha 1: pedimos ao usuário que insira um número inteiro que determinará quantos elementos essa lista terá 

#Linha 3: cria essa lista de maneira indeterminada

#Linha 5/Primeiro for: iremos iterar 'i' de 0 até o número 3, o que foi determinado pela estrutura 'in range' 
    #Ao utilizarmos lista.append() utilizamos um método que adicionará ao final da lista elementos que forem digitados pelo usuário


#Linha 10/Segundo for: aqui verificaremos se um elemento é par ou ímpar por meio do if, podemos utilizar 'if' ou apenas 'if not', o que seria '=' e '!='
    #Ao utilizarmos lista.pop() eliminamos o elemento da lista na posição indicada entre parentêses                         
    
