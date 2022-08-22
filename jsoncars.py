from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    c = Counter()
    for i in data:
        if i["year"] == year:
            c.update([i["automaker"]])
    return c.most_common(1)[0][0]
    pass


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    models = set()
    for i in data:
        if i["automaker"] == automaker and i["year"] == year:
            models.add(i["model"])
    return models
    pass
