import random

import requests

from BasicWord import BasicWord

"""Импортируйте нужные классы и функции."""


def _load_data(path):
    """Функция каторая загружает данные"""
    return requests.get(path).json()


def load_data(path):
    """Загружает данные по ссылке и возвращает экземпляр класса BasicWord"""
    data = _load_data(path)
    random_word = random.choice(data)
    word_result = BasicWord(
        word=random_word['word'],
        subwords=random_word['subwords'])
    return word_result