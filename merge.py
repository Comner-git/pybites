from collections import defaultdict

NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    combined_dict = defaultdict(list)
    for group in (group1, group2, group3):
        for key, value in group.items():
            combined_dict[key].append(value)
    try:
        return combined_dict[name.lower()][-1]
    except:
        return NOT_FOUND
    pass
