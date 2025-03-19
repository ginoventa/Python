import random 
        
def jogadorGanhou():
    print("Jogador ganhou")

def maquinaGanhou(): 
    print("Maquina ganhou")

maquina = ['rock', 'paper', 'scissor']

jogador =  input("Qual sua opção: ").lower()

maquina = random.choice(maquina)

print(maquina)

if maquina == 'rock':
    if jogador == 'paper':
        jogadorGanhou()
    elif jogador == 'scissor': 
        maquinaGanhou()
    else: 
        print("Empate")
elif maquina == 'paper':
    if jogador == 'rock':
        maquinaGanhou()
    elif jogador == 'scissor': 
        jogadorGanhou()
    else: 
        print("Empate")
elif maquina == 'scissor':
    if jogador == 'paper':
        maquinaGanhou()
    elif jogador == 'rock': 
        jogadorGanhou()
    else:
        print("Empate")

#Apesar de sua estrutura simples, sobre o método 'choice':
  ##O método choice() é utilizado para devolver de uma sequência definida um elemento aleatório, nos moldes definidos pela sequência
