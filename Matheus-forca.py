#importar o random para sortear algo
import random
#criar variáveis
#criar lista
palavras = []
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def juniscreide():
    while True:
        juniscreide = input('escreva uma palavra: ')
        palavras.append(juniscreide)
        if juniscreide == '':
            break
#serve para criar funções
#todo o programa vai funcionar em torno da função principal
def principal():
    """
    Função Princial do programa
    """
    juniscreide()
    #imprimir algo na tela
    print('F O R C A')

    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)
    #serve para executar algo enquanto uma coisa for verdade
    while True:
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        #serve como condição(se...)
        if perdeuJogo():
            print('Voce Perdeu!!!')
            #parar com o programa
            break
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
        
def perdeuJogo():
    # serve para alterar o valor de uma variável para global dentro de uma função
    global FORCAIMG
    #(len)retorna um valor do tipo inteiro, representando a quantidade de caracteres contido na string
    if len(letrasErradas) == len(FORCAIMG):
        #se for verdade, retorne!
        return True
    #se não, então...
    else:
        #se for falso, retorne!
        return False
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    #verdade
    ganhou = True
    #para ***** em ***** então faça...
    for letra in palavraSecreta:
        #se **** não está em ***** então...
        if letra not in letrasCertas:
            ganhou = False 
    #retornar para a variável
    return ganhou        
        


def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
    else:
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        #gerar uma lista ou a quantidade de vezes que o loop será executado
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()

    
principal()

