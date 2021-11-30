import pytest
from unittest.mock import patch
import urllib.request
import json


API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def test_ymd_format():
    """Проверяем правильность работы при формате YYYY-MM-DD"""
    date = dict(currentDateTime='2021-11-30')
    expected = 2021
    with patch.object(urllib.request, 'urlopen'), \
         patch.object(json, 'load', return_value=date):
        actual = what_is_year_now()

    assert actual == expected


def test_dmy_format():
    """Проверяем правильность работы при формате DD.MM.YYYY"""
    date = dict(currentDateTime='30.11.2021')
    expected = 2021
    with patch.object(urllib.request, 'urlopen'), \
         patch.object(json, 'load', return_value=date):
        actual = what_is_year_now()

    assert actual == expected


def test_wrong_format():
    """Учитываем случай с неверным форматом"""
    date = dict(currentDateTime='2021/11/30')
    with patch.object(urllib.request, 'urlopen'), \
         patch.object(json, 'load', return_value=date):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_wrong_key():
    """Учитываем случай с неверным ключом"""
    date = dict(ordinalDate='2021-334')
    with patch.object(urllib.request, 'urlopen'), \
         patch.object(json, 'load', return_value=date):
        with pytest.raises(KeyError):
            what_is_year_now()


def test_wrong_value():
    """Учитываем случай с неверным значением"""
    date = dict(currentDateTime='2021')
    with patch.object(urllib.request, 'urlopen'), \
         patch.object(json, 'load', return_value=date):
        with pytest.raises(IndexError):
            what_is_year_now()


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)
