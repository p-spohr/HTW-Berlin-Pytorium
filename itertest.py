# itertest.py
# %%
import itertools as it
import operator
# %%

nums = list(range(0,11,1))

# %%

list(it.repeat(0, 10))
# %%

list(it.accumulate(nums, operator.add))

# %%

list(it.accumulate(nums[1:], operator.mul))

# %%

list(it.batched(nums, 2))

# %%

nums2 = list(it.chain(nums, nums))

# %%

# returns all numbers in a list that are even and not zero
list(it.compress(nums2, [True if num % 2 == 0 and num != 0 else False for num in nums2]))

# %%

list(filter(lambda x : x < 2, nums2))

# %%

list(it.permutations('ABCD', 2))

# %%

list(it.combinations('ABCD', 2))

# %%

list(it.combinations_with_replacement('ABCD', 2))

# %%
import math
# %%

math.remainder(9,2)

# %%

import fractions

# %%

fractions.Fraction(10,8)

# %%

fractions.Fraction(0.25)
