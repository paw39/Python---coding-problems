import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element

print(pick([1,2,3,4,5,6,7,5345,345345,435,34,5,345,2234,56,24534,25,2]))