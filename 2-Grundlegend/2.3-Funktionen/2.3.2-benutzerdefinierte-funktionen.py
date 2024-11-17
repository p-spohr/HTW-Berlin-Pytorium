
# %%

def hallo():
    print('Hallo!')

# %%

hallo()

# %%

# hallo ohne () ist die Funktion im Speicher.
hallo

# %%

# Die Funktion selbst kann gespeichert werden
hallo2 = hallo
hallo2()

# %%

# name heißt Parameter
def hallo_name(name):
    print(f'Hallo, {name}')

# %%

# 'Karl' ist der Argument, den in Name-Parameter fließt
hallo_name(name='Karl')

# %%

# probe ist eine Liste
def mittelwert(probe):
	summe = sum(probe)
	return summe / len(probe)

# %%

mittelwert([1,2,3])

# %%

mittelwert((1,2,3))

# %%

mittelwert(range(0,10,1))

# %%

def add_me(*args):
    temp = 0
    for num in args:
        temp += num
    return temp

# %%

add_me(1,2,3)

# %%

add_me(*[1,2,3])
# %%
add_me(*(1,2,3))

# %%
def mannschaft(*spieler):
    anzahl = len(spieler)
    temp = 'Die Mannschaft hat '
    for s in spieler:
        anzahl -= 1
        if anzahl > 0:
            temp += f'{s}, '
        else:
            temp += f'und {s}'
    temp += '.'
    return temp

# %%

mannschaft('Bob', 'Tim', 'Tina')

# %%

def tier(**kwargs):
    print(f'{kwargs['name']}')
    print(f'{kwargs['alter']}')
    print(f'{kwargs['besitzer']}')
    print(f'{kwargs['art']}')

# %%

tier(name='Spot', alter=2, besitzer='Frankie', art='Hund')

# %%

# Mit Anmerkungen kann man Hinweise geben
def mittelwert_anmerk(probe: list) -> float:
    """
    Rechnet den Mittelwert
    """
    summe = sum(probe)
    return summe / len(probe)

# %%

mittelwert_anmerk([1,2,3])

# %%