class WordValidator:
    def is_valid_word(self, word):
        if len(word) == 4 and word.isalpha():
            return True
        else:
            return False