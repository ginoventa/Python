from random import randint

def randomNumberGenerator():
    return str(randint(1000,9999))

def main():

    number = str(randomNumberGenerator())
    print(number)
    guess = input("Guess the number: ")
    
    for i in range(len(number)): 
        if guess[i] == number[i]: 
            print("Cow")
        else:
            print("Bull")

if __name__ == "__main__": 
    main()


#Para fazer esse exercício utilizamos da ideia da string para conseguir separar um único número em diversos, como se fosse um vetor de char

#Explicação 

#Linha 1: estamos importando uma biblioteca, mas mais especificamente um método dela, o randint
    #Esse método é responável por gerar, no determinado intervalo, um número aleatório
    #Linha 4: neste caso, para que possamos fazer a comparação posteriormente, forçamos que o número seja devolvido como um vetor de char

#Linha 10: pedimos o número para o usuário, em forma de string também

#Linha 12/Estrutura for: a estrutura está iterando do número 0 ('i' inicialmente) até o número 4(tamanho do vetor de char number)
    #Caso o vetores de char sejam compatíveis nas posições esperadas o app printa "Cow", caso contrário, printa "Bull"

#Linha 18: tal estrutura é utilizada para garantir que nenhuma outra função seja chamada no lugar da main, como, por exemplo, uma main pré-definida 
#pelo programa
