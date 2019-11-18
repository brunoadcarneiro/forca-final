
import random

FORCA = ['''
 
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

palavras = 'formiga babuino encefalo elefante girafa hamburger chocolate giroscopio'.split()

def main():
    
    global FORCA
 
    print('F O R C A')
    letrasErradas = '' 
    letrasAcertadas = '' 
    palavraSecreta = geraPalavraAleatoria().upper()
    jogando = True
 
    while jogando: 
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta) 
 
        palpite = recebePalpite(letrasErradas + letrasAcertadas) 
 
        if palpite in palavraSecreta:
            letrasAcertadas += palpite 
 
            if VerificaSeGanhou(palavraSecreta, letrasAcertadas): 
                print("Parabens! A palavra secreta e "+palavraSecreta+'! Voce ganhou!!')
                jogando = False
        else:
            letrasErradas += palpite 
 
            if len(letrasErradas) == len(FORCA) - 1: 
                imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta) 
 
                print("Voce exagerou o seu limite de palpites!")
                print("Depois de "+str(len(letrasErradas))+' letras erradas e'+str(len(letrasAcertadas)), end = ' ')
                print('palpites corretos, a palavra era '+palavraSecreta+'.')
 
                jogando = False
 
        if not jogando:
            if JogarNovamente(): 
                letrasErradas = '' 
                letrasAcertadas = '' 
                jogando = True
                palavraSecreta = geraPalavraAleatoria().upper() 
                
def geraPalavraAleatoria():
    
    global palavras
    return random.choice(palavras)

def imprimeComEspacos(palavra):
    
    for letra in palavra:
        print(letra, end = ' ')
 
    print()
 

def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    
    global FORCA 
    print(FORCA[len(letrasErradas)]+'\n')  
 
    print("Letras Erradas:", end = ' ') 
    imprimeComEspacos(letrasErradas) 
 
    vazio = '_'*len(palavraSecreta) 
    for i in range(len(palavraSecreta)): 
        if palavraSecreta[i] in letrasAcertadas: 
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:] 
 
    imprimeComEspacos(vazio) 

def recebePalpite(palpiteFeitos):
    ''' Essa funcao garante que o usuario digite so uma letra e que confere se a mesma ja foi chutada '''
    
    while True: 
        palpite = input('Adivinhe alguma letra. \n').upper() 
        
        if len(palpite) != 1: 
            print('Coloque uma unica letra')
        elif palpite in palpiteFeitos: 
            print('Voce ja digitou essa letra, digite de novo!')
        elif not 'A' <= palpite <= 'Z': 
            print('Escolha Somente uma letra!')
        else:
            return palpite  

def JogarNovamente():
    
    return input("Voce quer jogar novamente? (sim ou nao)\n").upper().startswith('S') 
 
def VerificaSeGanhou(palavraSecreta, letrasAcertadas):
    ganhou = True
    for letra in palavraSecreta: 
        if letra not in letrasAcertadas: 
            ganhou = False 
            break 
 
    return ganhou
 
main()
                           
        
    
    
    
