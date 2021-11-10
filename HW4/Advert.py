import json
from keyword import iskeyword


class ObjectTransformer:
    """
    Transform JSON object to Python dict.
    """
    def __init__(self, mapping):
        if not isinstance(mapping, dict):
            raise 'Object type should be dict.'
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                self.__dict__[key] = ObjectTransformer(value)
            else:
                self.__dict__[key] = value


class ColorizeMixin:
    """
    Helps to change text color, the background color and add styles.
    """
    def __init__(self, style=1, text_color=32, bg_color=40):
        self.style = style
        self.text_color = text_color
        self.bg_color = bg_color

    def __str__(self):
        return f'\033[{self.style};{self.text_color};{self.bg_color}m {self.__repr__()}'


class Advert(ColorizeMixin):
    """
    The class of advertising that is initialized by json data format. It has one required field "title."
    """
    def __init__(self, mapping):
        ColorizeMixin.__init__(self)
        mapping_transformed = ObjectTransformer(mapping).__dict__
        if 'title' not in mapping_transformed:
            raise ValueError('Field "title" is required.')
        if 'price' in mapping_transformed:
            self.price = mapping_transformed['price']
        self.__dict__.update(mapping_transformed)

    def __repr__(self):
        return f'{self.title} | {self._price} ₽'

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError('Price should be greater than 0.')
        self._price = new_price


if __name__ == '__main__':
    lesson_str = """{
        "title": "python",
        "price": 100,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    # обращаемся к атрибуту location.address
    print(lesson_ad.location.address)
    print(lesson_ad)
