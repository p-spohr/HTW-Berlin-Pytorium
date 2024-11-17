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

import ersterOrdner.zweiterOrdner.greetings

# %%

ersterOrdner.zweiterOrdner.greetings.say_hello('patrick')

# %%

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self, food='grub'):
        print(f'Yum! Thanks for the {food}!')

# %%

class Pet(Animal):

    def __init__(self, owner, name):
        self.owner = owner
        super().__init__(name)

    def eat(self,food='grub'):
        super().eat(food)

    def pet(self):
        print('Happiness ++++++')

# %%

my_animal = Animal('Snowbub')

# %%

my_animal.name

# %%

my_pet = Pet('Pat', 'Spot')

# %%

my_pet.name

# %%

my_pet.owner
# %%

my_pet.eat('pasta')

# %%

my_pet.eat()

# %%

my_pet.pet()

# %%
