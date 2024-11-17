# %%

print('Hi!')

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
