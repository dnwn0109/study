import random

random_list = []

def random_genlist(a):
    for i in range(a):
        random_list.append(random.randint(1,6))
    return random_list