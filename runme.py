# %%
x = 10
print(x * 10)
# %%
def hello(name):
    if type(name) != str: raise TypeError('Please input type str')
    print(f'Hello, {name}!')
# %%
hello('Tim')
# %%
hello(90)

# %%
for item in dir():
    print(item)
# %%

name_input = input('Please input name: ')
# %%
name_input
# %%
dir()
# %%
dict(name='Bob', age=50, city='Berlin')
# %%
n = 45.24912
# %%
f'{n:0.2f}'
# %%
hello.__call__('Bill')
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
