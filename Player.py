class Player:

    def __init__(self, player_name=""):
        self.player_name = player_name

        self.word_list = []

    def __repr__(self):
        return f"Player(player_name='{self.player_name}')"

    def get_word_count(self):
        """Получение количества угаданных слов"""
        return len(self.word_list)

    def add_word(self, word):
        """Добавление слова пользователя"""
        self.word_list.append(word)

    def unique_list(self, word):  # Список должен быть уникальным
        """Проверка использования данного слова до этого (возвращает bool)."""
        return word in self.word_list

    def get_player_name(self):
        """Получение имени пользователя"""
        return self.player_name

