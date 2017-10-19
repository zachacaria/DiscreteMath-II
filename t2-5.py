import itertools
import random

def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))

permut = itertools.permutations(random_permutation(range(1,101), 5))

count_permut = []
for i in permut:
    count_permut.append(i)

a =  count_permut[0:100]

for i in a:
    print  a.index(i)+1, i
