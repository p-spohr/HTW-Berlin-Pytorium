# %%
import random
import time
# %%

lange_liste = list(range(1,10_000_000,1))

random.shuffle(lange_liste)
# %%
def cumsum(liste):
    temp = 0
    for index, num in enumerate(liste):
        temp += num
        liste[index] = round(temp, 4)
    return liste
# %%
# start_time = time.time()
# cumsum(lange_liste)
# end_time = time.time()
# print(round(end_time - start_time,2))
# %%

import numpy as np

# %%

np_array = np.array(lange_liste)

# %%

np_array.cumsum()

# %%

np_array.max()

# %%
np_array.mean()

# %%

import requests

data = requests.get('https://gist.githubusercontent.com/craigh411/19a4479b289ae6c3f6edb95152214efc/raw/d25a1afd3de42f10abdea7740ed098d41de3c330/List%2520of%2520the%25201,000%2520Most%2520Common%2520Last%2520Names%2520(USA)')

# %%

def remove_comma(word: str) -> str:
    return word[:-1]

# %%
raw_names = data.content.decode().split('\n')
my_names = map(remove_comma, raw_names)

# %%

import pandas as pd

pd.DataFrame(my_names, columns=['Lname'])

# %%

data.content

# %%

pd.DataFrame(data.content.decode().split(',\n'),columns=['LName'])

# %%

import numpy as np

# %%

def add(a,b):

    return a+b

simp_sum = map(add, [1,1,1], [1,1,1])

print(list(simp_sum))

# %%

ones = np.full((2,3), 1)

# %%

np.array(([[1,1,1],
           [1,1,1]]))

# %%

np.apply_along_axis(add, 0, *ones)

#%%


# %%

ones.sum(axis=1)

# %%

a = np.arange(24).reshape(2,3,4)
print(a)

# %%

a.max(axis=0)

# %%

np.apply_over_axes(np.max, a, axes=[0,1])

# gleicher Befehl
# a.max(axis=0).max(axis=0)
