from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(promo, name, expires):
        promo.name = name
        promo.expires = expires
        promo._expired = False
        if promo.expires <= NOW:
            promo._expired = True
        else:
            promo._expired = False

    def getter(promo):
        return promo._expired

    def setter(promo, expires):
        pass

    expired = property(getter, setter)
