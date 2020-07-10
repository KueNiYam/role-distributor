import random
import copy

def distribute_role(roles, people):
    copied = copy.deepcopy(people)
    random.shuffle(copied)
    return dict(zip(roles, copied))