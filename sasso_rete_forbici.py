import os 
import random
import time

items = ['SASSO', 'RETE', 'FORBICI']

def menu():
    
    print(''' 
[S] START
[E] EXIT
    ''')

    start = input()
    if start == 'S' or start == 's':
        startGame()
    elif start == 'E' or start == 'e':
        esci = input('Desideri uscire dal gioco? S/n ')
        if esci == 'S' or esci == 's':
            print('Attendere...')
            time.sleep(1)
            print('PROGRAMMA TERMINATO!')
            exit()
        elif esci == 'N' or esci == 'n':
            menu()

def startGame():
    punteggioPl1 = 50
    punteggioPC = 50
    
    while True:
        time.sleep(1)
        print('\nSASSO, RETE, FOR-BI-CI!')
        time.sleep(2)
        scelta = input('''
        
SASSO 
RETE 
FORBICI 
        
''')
        if scelta == 'SASSO' or scelta == 'Sasso' or scelta == 'sasso':
            print('HAI SCELTO SASSO')
            iaElem = ia(items)
            print('IL PC HA SCELTO: ', iaElem)
            if iaElem == 'SASSO':
                print('PAREGGIO!')
            elif iaElem == 'RETE':
                print('IL COMPUTER VINCE!')
                punteggioPl1 -= 10
                print('Il tuo punteggio scende di 10 punti, ', punteggioPl1, "punti")
                if punteggioPl1 == 0:
                    print('HA VINTO IL PC!')
                    print('Punti totali pc: ', punteggioPC, "punti")
                    time.sleep(5)
                    menu()
            elif iaElem == 'FORBICI':
                print('HAI VINTO!')
                punteggioPC -= 10
                print('Il punteggio del pc scende di 10 punti, ', punteggioPC, "punti")
                if punteggioPC == 0:
                    print('HAI VINTO LA PARTITA!')
                    print('Punti totali umano: ', punteggioPl1, "punti")
                    time.sleep(5)
                    menu()

        if scelta == 'RETE' or scelta == 'Rete' or scelta == 'rete':
            print('HAI SCELTO RETE')
            iaElem = ia(items)
            print('IL PC HA SCELTO: ', iaElem)
            if iaElem == 'SASSO':
                print('HAI VINTO!')
                punteggioPC -= 10
                print('Il punteggio del pc scende di 10 punti, ', punteggioPC, "punti")
                if punteggioPC == 0:
                    print('HAI VINTO LA PARTITA!')
                    print('Punti totali umano: ', punteggioPl1, "punti")
                    time.sleep(5)
                    menu()
            elif iaElem == 'RETE':
                print('PAREGGIO')
            elif iaElem == 'FORBICI':
                print('IL COMPUTER VINCE')
                punteggioPl1 -= 10
                print('Il tuo punteggio scende di 10 punti, ', punteggioPl1, "punti")
                if punteggioPl1 == 0:
                    print('HA VINTO IL PC!')
                    print('Punti totali pc: ', punteggioPC, "punti")
                    time.sleep(5)
                    menu()
            
        if scelta == 'FORBICI' or scelta == 'Forbici' or scelta == 'forbici':
            iaElem = ia(items)
            print('IL PC HA SCELTO: ', iaElem)
            if iaElem == 'SASSO':
                print('IL COMPUTER VINCE!')
                punteggioPl1 -= 10
                print('Il tuo punteggio scende di 10 punti, ', punteggioPl1, "punti")
                if punteggioPl1 == 0:
                    print('HA VINTO IL PC!')
                    print('Punti totali pc: ', punteggioPC, "punti")
                    time.sleep(5)
                    menu()
            elif iaElem == 'RETE':
                print('HAI VINTO!')
                punteggioPC -= 10
                print('Il punteggio del pc scende di 10 punti, ', punteggioPC, "punti")
                if punteggioPC == 0:
                    print('HAI VINTO LA PARTITA!')
                    print('Punti totali umano: ', punteggioPl1, "punti")
                    time.sleep(5)
                    menu()       
            elif iaElem == 'FORBICI':
                print('PAREGGIO!')

def ia(elements):
    rand = random.choice(items)
    return rand

menu()
os.system('pause')
