import numpy as np

for i in range(4):
    np.array(i, i + 1)
    print(i)

lest = [
    'this is a very long list that will go over the max line length',
    'test another',
    'test another',
    'test another',
    'test another',
]


def my_func(var: str) -> str:
    """Add 1 to whatever"""
    return var + str(1)
