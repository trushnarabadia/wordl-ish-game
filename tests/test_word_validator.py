from game.word_validator import WordValidator

def test_valid_four_letter_word():
    validator = WordValidator()
    assert validator.is_valid_word("test") == True

def test_rejects_words_too_short():
    validator = WordValidator()
    assert validator.is_valid_word("cat") == False

def test_rejects_words_too_long():
    validator = WordValidator()
    assert validator.is_valid_word("hello") == False