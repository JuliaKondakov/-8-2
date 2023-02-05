from BasicWord import BasicWord
from Player import Player
from utils import load_data

DATA_JSON_URL = "https://api.npoint.io/ab3727d36ef2972d7006"

print("Введите имя игрока")
user_name = input()
"""Поздоровайтесь с пользователем"""
real_player = Player(player_name=user_name)

print(f"Привет, {real_player.get_player_name()}")


start_words = load_data(DATA_JSON_URL)


print(f"Составьте {start_words.all_subword_count()} слов из слова {start_words.get_word()}")
print(f"Слова должны быть не короче 3 букв")
print(f"Чтобы закончить игру, угадайте все слова или напишите \'stop\'")
print(f"Поехали, ваше первое слово?")

while real_player.get_word_count() < start_words.all_subword_count():

    """Запуск цикла, пока не закончится слова (word)"""
    user_input: str = input().lower().strip()
    """Если слово stop или стоп, то игра прекращается"""

    if user_input in ["stop", "стоп"]:
        print(f" Игра завершена, вы угадали")
        break

    elif len(user_input) < 3:
        """Если слово короче 3 букв выводит"""
        print("слишком короткое слово")

    elif user_input not in start_words.get_subwords():
        print("неверно")

    elif real_player.unique_list(user_input) is True:
        print("УЖЕ БЫЛО")

    elif user_input in start_words.get_subwords():
        """Верно, угаданное слово добовляем в список угаданных"""
        print("верно")
        real_player.add_word(user_input)
        print(real_player.word_list)

        """Игра закончилась, выводим статистику количества угаданных слов """
print(f"Игра завершена, вы угадали {real_player.get_word_count()} слов!")