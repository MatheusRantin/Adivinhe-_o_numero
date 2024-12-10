import random
import os
import time



def startGame():
    print("JOGO ADIVINHE O NÚMERO")
    print("Nesse jogo a regra é simples, o computador da selecionar um \nnúmero aleatório e você deverá adivinhar qual é este valor")
    print("Pressione ENTER para continuar...")
    input('Aperte ENTER para continuar ...')
    os.system('cls')

def gameRules():
    print("Beleza então, Vejo que está ansioso para começar a jogar \nmas antes disso veja as regras abaixo:\n")
    print(' 1. Só é valido números inteiros \n 2. O número selecionado deve ser escolhido entre os valores de 1 á 10\n')
    print('Com isso em mente aperte ENTER para começar...')
    input('Pressione ENTER para continuar ...')
    os.system('cls')

def game(selectNumber):
    selectNumber = int(selectNumber)
    number = random.randrange(1,10)
    if number == selectNumber:
        print(f'Parabéns você acertou o número:\n Número do Computador = {number}\n Seu Número = {selectNumber} ')
    elif number != selectNumber:
        print(f'😫 Infelizemente você ERROUUUUU, não foi dessa vez:\n Número do Computador = {number}\n Seu Número = {selectNumber} ')
    
        
        

def callGame():
    while True:
        startGame()
        gameRules()
        numero = input('Seu número:')
        print(f'Seu número escolhido foi {numero}')
        game(numero)
        optionUser = int(input("1. Jogar novamente \n2. Sair\nDigite uma das opções: "))
        if optionUser == 1:
            continue
        elif optionUser == 2:
            break

if __name__ == '__main__':
    callGame()