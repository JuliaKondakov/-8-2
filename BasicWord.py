class BasicWord:
    def __init__(self, word="", subwords=None, ):

        if subwords is None:

            self.subwords = []

        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f"BasicWord(word='{self.word}', subwords={self.subwords})"

    def get_word(self):
        return self.word

    def get_subwords(self):
        return self.subwords

    def is_correct(self, user_answer):
        """Проверку введенного слова в списке допустимых подслов"""
        return user_answer() in self.subwords

    def all_subword_count(self):
        """Подсчет количества подслов (вернет int)"""
        return len(self.subwords)