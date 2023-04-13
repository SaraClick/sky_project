from random import choice

# Function to randomly select one URL from the list of URL's provided
# random.choice(list) Choose a random item from a sequence. Here seq can be a list, tuple, string, or any iterable like range.


def select_random_from_list(my_list):
    selected = choice(my_list)
    return selected

