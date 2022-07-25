from typing import Dict, List

cars = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}
DEFAULT_SEARCH = "trail"
CarsType = Dict[str, List[str]]


def get_all_jeeps(cars: CarsType = cars) -> str:
    """
    Retrieve the 'Jeep' models from the cars dict and join them by a
    comma and space (', '). Leave the original ordering intact.
    """
    s = ", "
    jeep_string = s.join(cars["Jeep"])
    return jeep_string
    pass


def get_first_model_each_manufacturer(cars: CarsType = cars) -> List[str]:
    """
    Loop through the cars dict filtering out the first model for each
    manufacturer. Return the matching models in a list leaving the original
    ordering intact.
    """
    firstmodel = []
    for key, value in cars.items():
        firstmodel.append(value[0])
    return firstmodel
    pass


def get_all_matching_models(
    cars: CarsType = cars, grep: str = DEFAULT_SEARCH
) -> List[str]:
    """
    Return a list of all models containing the case insensitive
    'grep' string which defaults to DEFAULT_SEARCH ('trail').
    Sort the resulting sequence alphabetically
    """
    def search(dictionary, searchString):
        list = [
            s for val in dictionary.values() for s in val if searchString.lower() in s.lower()
        ]
        list.sort()
        return list
    print(search(cars, grep))
    return search(cars, grep)
    pass


def sort_car_models(cars: CarsType = cars) -> CarsType:
    """
    Loop through the cars dict returning a new dict with the
    same keys and the values sorted alphabetically.
    """
    for make, model in cars.items():
        model.sort()
        cars[make] = model
    sort = dict(sorted(cars.items()))
    return sort
    pass
