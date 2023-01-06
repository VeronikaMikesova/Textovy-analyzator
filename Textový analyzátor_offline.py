# úvodní informace
print("""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Veronika Mikešová
email: veronikamikesova@gmail.com
discord:
""")
# vstupní data
oddelovac = "-"*62
print(oddelovac)
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
# slovník uživatelů
user_1 = {"prihlasovaci_jmeno":"bob", "heslo":"123"}
user_2 = {"prihlasovaci_jmeno":"ann", "heslo": "pass123"}
user_3 = {"prihlasovaci_jmeno":"mike", "heslo": "password123"}
user_4 = {"prihlasovaci_jmeno":"liz", "heslo": "pass123"}
registered_users = (user_1, user_2, user_3, user_4)

# přihlášení uživatele a jeho kontrola
prihlasovaci_jmeno = input("username:")
heslo = input("password:")
user_5 = {"prihlasovaci_jmeno":prihlasovaci_jmeno, "heslo":heslo}

for users in registered_users:
    if user_5 != users:
        print("unregistered user, terminating the program")
        quit(),
    else:
        print(f"Welcome to the app, {prihlasovaci_jmeno}\nWe have 3 texts to be analyzed.\n{oddelovac}") 
        break

number = input("Enter a number btw. 1 and 3 to select:") 
if not number.isnumeric(): 
    print("Incorrect input"),
    quit(),
elif int(number) not in range (1,4):
    print("Incorrect input"),
    quit(),
else:
    selected_text = TEXTS[int(number)-1]
    seznam_slov0 = selected_text.split()   # vytvoří seznam s určitým počtem položek, slova jsou oddělena mezerami, al ještě neočištěn o znaky

seznam_slov = list()
for slovo in seznam_slov0:
    seznam_slov.append(slovo.strip(".,"))
print(f"There are {len(seznam_slov)} words in the selected text.")

inicialy = list()
for slovo in seznam_slov:  # výběr slov s velkým písmenem na začátku
    if slovo[0].isupper():
       inicialy.append(slovo[0])
print(f"There are {len(inicialy)} titlecase words.")
    
velka_pismena = list()
for slovo in seznam_slov: # výběr slov všechna s velkými písmeny
    if slovo[:].isupper() and slovo.isalpha():
        velka_pismena.append(slovo)
print(f"There are {len(velka_pismena)} uppercase words.")

mala_pismena = list()
for slovo in seznam_slov: # výběr slov všechna s malými písmeny
    if slovo[:].islower():
        mala_pismena.append(slovo)
print(f"There are {len(mala_pismena)} lowercase words.")  

cifry = list()
for slovo in seznam_slov: # výběr slov, která jsou číslicemi
    if slovo.isnumeric():
       cifry.append(slovo)
print(f"There are {len(cifry)} numeric strings.")  

cisla = list()
for cislo in cifry: # string přetvoříme na čísla a vyrobíme nový seznam "cisla"
    cisla.append(int(cislo))
    soucet = sum(cisla) #sečteme položky nového seznamu
print(f"The sum of all the numbers {soucet}.")
print(oddelovac)

zahlavi = ("LEN", "OCCURENCES", "NR.")
print(f"{' | '.join(zahlavi)}", oddelovac, sep="\n")

sequence = list()
for slovo in seznam_slov:
    sequence.append(len(slovo))
counts = {}
for number in sequence:
    if number not in counts:
        counts[number] = 1
    else:
        counts[number] = counts[number] + 1
for key, value in sorted(counts.items()):
    print(key, "|", "*"*value, "|", value)


        

