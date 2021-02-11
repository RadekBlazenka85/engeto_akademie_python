import random

def main():
    pripraveni_hry()
    deska, hrac = nastaveni()
    while True:
        tisk(deska)
        deska = posun(hrac, deska)
        if kontrola(deska, hrac):
            konec(hrac)
            break
        elif cela_deska(deska):
            remiza()
            break
        hrac = vymena(hrac)
    tisk(deska)

def nastaveni():
    velikost = int(input('Please enter the board size: '))
    deska = []
    for radek in range(velikost):
        deska.append([' '] * velikost)
    start = random.choice(['x', 'o'])
    return deska, start

def pripraveni_hry():

    print('''

    ===========================
    Welcome to Tic Tac Toe
    GAME RULES:
    Each player can place one mark (or stone) per turn on the 3x3 grid
    The WINNER is who succeeds in placing three of their marks in a
    * horizontal,
    * vertical or
    * diagonal row
    Let's start the game

''', end='\n')

def tisk(deska):
    b = []
    velikost = len(deska)
    b.append('\n' + '-' * velikost * 2 + '\n')
    for radek in deska:
        b.append('|'.join(radek) + '\n')
        b.append('-' * velikost * 2 + '\n')
    print(''.join(b))

def posun(hrac, deska):
    while True:
        tah = int(input('Player {} | Please enter your move number:'.format(hrac)))
        radek, vklad = koordinaty(tah, len(deska))
        if deska[radek][vklad] == ' ':
            deska[radek][vklad] = hrac
            break
        else:
            print('\nThis position is already taken\n')
    return deska

def koordinaty(souradnice, velikost):
    sloupec = (souradnice - 1) % velikost
    radek = round((souradnice - sloupec) // velikost)
    return radek, sloupec

def vymena(hrac):
    return 'x' if hrac == 'o' else 'o'

def kontrola(deska, hrac):
    velikost = len(deska)
    h_deska = vyrovnat(deska)
    for i in range(velikost):
        if set(h_deska[i * velikost:i * velikost + velikost]) == set(hrac) \
 \
                or set(h_deska[i:velikost ** 2:velikost]) == set(hrac):
            return True
        if i == 0 and set(h_deska[i:velikost ** 2:velikost + 1]) == set(hrac):
            return True
        elif i == velikost - 1 and set(h_deska[i:velikost ** 2 - 1:velikost - 1]) == set(hrac):
            return True

def vyrovnat(deska):
    pole = []
    for radek in deska:
        pole += radek
    return pole

def konec(hrac):
    print('\n{}\n'.format('=' * 20))
    print('Congratulations, the player {} WON!'.format(hrac))

def cela_deska(deska):
    return ' ' not in vyrovnat(deska)

def remiza():
    print('\n{}\n'.format('=' * 20))
    print('Nobody wins, this is a tie')

main()