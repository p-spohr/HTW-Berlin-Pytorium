# %%

import erstesModul.filme.film
# import time

# %%

favorite_film = erstesModul.filme.film.Film('Matrix', 1997, 5)

# %%

favorite_film.review()

# %%

favorite_film.info()

# %%

# time.sleep(3)

# %%

get_input = input('\nPress enter to exit...')
if get_input:
    quit()
# %%


def multipyme(a,b=5):
    a += 1
    return a * b


multipyme(10,10)


# %%


def multipyme(a,b=5):
    a += 1
    return a * b

multipyme(10,10)


# %%

print('Hello!')

# %%

print('Hello!')

print('-'*10)

# %%

print('Hello!')

# %%

list_a = []
list_b = list_c = []

# %%

list_a == list_b

# %%

list_a is list_b


# %%

list_b is list_c

# %%

list_b.append(1)

# %%

list_c.append(2)

# %%

list_d = list_c.copy()

# %%

list_d.append('NEW')

# %%

list_c

# %%

list_b

# %%
x_range = range(0,6,1)
list(map(lambda x : x + 1, x_range))


# %%

hungrig = True
if hungrig == True:
	print('Ich habe Hunger.')
else:
	print('Ich bin satt.')

# %%

zahl = int(input('Zahl: '))
match zahl:
	case 1:
		print("Eins")
	case 2:
		print("Zwei")
	case _:
		print("Eine andere Zahl")

# %%

gruppe = [
		  {'name': 'Tim', 'alter':55, 'essen': 'pizza'},
		  {'name': 'Tina', 'alter':33, 'essen': 'kuchen'},
		  {'name': 'Zed', 'alter':20, 'essen': 'schnitzel'}]

for freund in gruppe:
    match freund['name']:
        case 'Tina':
            print('Meine Beste Freundin!')
            print('Lass uns', freund['essen'], 'essen!')
        case _:
            print('Hallo.')

# %%

gruppe = [
		  {'name': 'Tim', 'alter':55, 'essen': 'pizza'},
		  {'name': 'Tina', 'alter':33, 'essen': 'kuchen'},
		  {'name': 'Zed', 'alter':20, 'essen': 'schnitzel'}]

for freund in gruppe:
	match freund['name']:
		case 'Tina':
			print('Meine Beste Freundin!')
			print('Lass uns', freund['essen'], 'essen!')
		case _:
			print('Hallo.')

# %%

dir()

# %%

def get_me(*,name, age):
	print(name, age)
# %%
get_me(name='Tim', age=22)
# %%

def add_me(a,b):
	return a + b
# %%
add_me(b=1, a=2)
# %%
new_list = []
new_list += [1,2,3]
print(new_list)
print(new_list.__eq__([1,2,3]))

# %%

x = 50
print(f'The variable {x=}')

# %%

import uuid

a_id = uuid.uuid1()
b_id = uuid.uuid1()
print(a_id == b_id)

# %%

print(uuid.uuid1())

print(uuid.uuid4())

# %%

class BesserList(list):

	def __new__(list, *args, **kwargs): 
		print("Creating instance of list") 
		instance = super().__new__(list, *args, **kwargs) 
		return instance
	
	def __init__(self, instance, besitzer):
		self.instance = instance
		self.besitzer = besitzer
		
	def minus_eins(self):
		return [x - 1 for x in self.instance]

# %%

neu_liste = BesserList([1,2,3,4], 'Patrick')

# %%

neu_liste.minus_eins()

# %%

neu_liste.__class__

# %%

neu_liste.besitzer

# %%

class BesserList2(list):
	def minus_eins(self):
		return [x - 1 for x in self]
	


# %%

BesserList2([1,2,3]).minus_eins()

# %%

class Person:
	def __new__(cls,*args,**kwargs):
		print(f'Eine Person ({args[0]}) wird geboren.')
		# print(cls)
		# print(Person)
		print(args)
		print(kwargs)
		return super(Person,cls).__new__(cls)
	def __init__(self, name):
		self.name = name

# %%

pat = Person('Pat')

# %%

print(pat.name)

# %%

import numpy as np

# %%

zahl = np.arange(10)

# %%

zahl.size

# %%

zahl.shape

# %%

zahl.ndim

# %%

zahl.reshape(2,5).max(axis=1)

# %%

zeros = np.zeros([3,3,3])

# %%

zeros[0][0] += 1

# %%

zeros.max(axis=2)
# %%

zeros
# %%

zeros1 = np.zeros([3,3])

# %%

zeros1[0] += 1

# %%

zeros1

# %%

zeros1.max(axis=1)

# %%

zeros1
# %%

zeros1[:,0]

# %%

class Base:
	def greet(self):
		print("Hallo von der Basisklasse")

class Derived(Base):
	def greet(self):
		super().greet()
		print("Hallo von der abgeleiteten Klasse")

d = Derived()
d.greet()
# %%
