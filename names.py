NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    names = list(set(names))
    new_names = [name.title() for name in names]
    return new_names
    pass

  
def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names, key=lambda x: x.split(" ")[-1], reverse=True)
    # ...


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    result = min(names, key=len)
    return result.rpartition(" ")[0]
    # ...
