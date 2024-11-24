# %%

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# %%


# %%

norm.ppf(0.5)

# %%

norm.cdf(0)

# %%

norm.pdf(0)

# %%

fig, ax = plt.subplots()
x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
ax.plot(x, norm.pdf(x))

# %% 

mean, var, skew, kurt = norm.stats(moments='mvsk')

print(mean, var, skew, kurt)

# %%

vals = norm.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], norm.cdf(vals))

# %%
fig, ax = plt.subplots()

r = norm.rvs(size=1000)

ax.hist(r, density=True, bins='auto', histtype='stepfilled', alpha=0.2)
ax.set_xlim([x[0], x[-1]])
ax.legend(loc='best', frameon=False)
plt.show()

# %%

fig, ax = plt.subplots()
lines = ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
# plt.show()                   

# %%

fig, ax = plt.subplots(figsize=(4, 3))
np.random.seed(19680801)
t = np.arange(100)
x = np.cumsum(np.random.randn(100))
lines = ax.plot(t, x)
# %%
