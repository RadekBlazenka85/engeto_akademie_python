'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

UCTY = ['bob', '123' , 'ann' , 'pass123' , 'mike' , 'password123' , 'liz' , 'pass123' , ]
ODDELOVAC = ('='*20)
print(ODDELOVAC)
print('Vítejte v aplikaci, prosím přihlašte se: ',)

JMENO = input('Uživatelské jméno: ',)
HESLO = input ('Heslo: ',)
print(ODDELOVAC)


if JMENO and HESLO in UCTY:
    print('Přihlášeno')

else:
    print('Uživatelské jméno, nebo heslo je špatně!')
    exit()
    quit()

print(ODDELOVAC)


print('Vyber tři texty')
VYBER = int(input('Vlož číslo od 1 do 3: '))

print(ODDELOVAC)

text = TEXTS[VYBER-1]

RUZNA_SLOVA = text.split()

slova = []


while RUZNA_SLOVA:

    slovo = RUZNA_SLOVA.pop()

    slovo = slovo.strip('.,:/;')

    if slovo: slova.append(slovo)


print('Ve vybraném textu je' , str(len(slovo)) , 'slov.')

velka_pocatecni_pismena = 0
velka_pismena = 0
mala_pismena = 0
cisla = 0
pocet_cisel = {}
sumarizace = 0

promenna = 0

while promenna < len(slova):
    if slova[promenna].istitle():
        velka_pocatecni_pismena = velka_pocatecni_pismena + 1
    elif slova[promenna].isupper():
        velka_pismena = velka_pismena + 1
    elif slova[promenna].islower():
        mala_pismena = mala_pismena +1
    elif slova[promenna].isnumeric():
        cisla = cisla + 1
        sumarizace = sumarizace + float(slova[promenna])

    l = len(slova[promenna])
    pocet_cisel[l] = pocet_cisel.get(l, 0) + 1

    promenna = promenna + 1

print('Ve vybraném textu je' , str(velka_pocatecni_pismena) , 'slov začínajících velkým písmenem.')
print('Ve vybraném textu je' , str(velka_pismena) , 'slov psaných velkými písmeny.')
print('Ve vybraném textu je' , str(mala_pismena) , 'slov psaných malými písmeny.')
print('Ve vybraném textu je' , str(cisla) , 'čísel.')

print(ODDELOVAC)


delky = sorted(pocet_cisel)
promenna = 0

while promenna < len(delky):
    delka = delky[promenna]
    frekvence = pocet_cisel[delka]

    if len(str(delka)) == 1:
        string_delka = '' + str(delka)

    else:
        string_delka = str(delka)

    print(string_delka, '*' * frekvence, frekvence)

    promenna = promenna + 1

print(ODDELOVAC)


print('Součet všech čísel v textu je: ', str(sumarizace))

print(ODDELOVAC)


print('KONEC PROGRAMU')
exit()
quit()

