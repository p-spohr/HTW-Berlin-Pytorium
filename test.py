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
