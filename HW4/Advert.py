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
            if key == 'price':
                key = '_price'
            if isinstance(value, dict):
                self.__dict__[key] = ObjectTransformer(value)
            else:
                self.__dict__[key] = value


class ColorizeMixin:
    """
    Helps to change text color, the background color and add styles.
    """
    style = 1
    text_color = 32
    bg_color = 40

    def __str__(self):
        return f'\033[{self.style};{self.text_color};{self.bg_color}m {self.__repr__()} \033[0m'


class Advert(ColorizeMixin, ObjectTransformer):
    """
    The class of advertising that is initialized by json data format. It has one required field "title."
    """
    def __init__(self, mapping):
        super().__init__(mapping)
        if not hasattr(self, 'title'):
            raise ValueError('Field "title" is required.')
        if hasattr(self, '_price'):
            if not isinstance(self._price, (int, float)):
                raise ValueError('Unsupported type of price.')
            if self._price < 0:
                raise ValueError('Price should be greater than 0.')

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    @property
    def price(self):
        return self._price

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
    lesson_address = 'город Москва, Лесная, 7'
    assert lesson_ad.location.address == lesson_address

    keyword_str = """{
            "title": "python",
            "price": 100,
            "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"]
            },
            "class": "Key word"   
        }"""
    keyword_ad = json.loads(keyword_str)
    keyword_check = Advert(keyword_ad)
    class_key = 'Key word'
    assert keyword_check.class_ == class_key

    print(keyword_check)

