# %%

import filme.film
import funktionen
import haustiere

import filme

# %%

meine_katze = haustiere.Katze('Snow', 2)

# %%

meine_katze.meow()

# %%

funktionen.greeting('Helga', 'Tina')

# %%

funktionen.add(1,2)

# %%

mein_film = filme.film.Film('Matrix', 1999, 5)

# %%

mein_film.review()

# %%

mein_film.info()

# %%

num = list(range(1, 11))

# %%
num
# %%

def plus_eins(a):
    return a + 1

num_map = map(plus_eins, num)

# %%

list(num_map)
    
# %%

list(enumerate(num_map))

# %%
# Anzahl von Iterable sollte die Anzahl der Parametern der Funktion sein
add_num = map(funktionen.add, num, num)
# %%
list(add_num)
# %%
