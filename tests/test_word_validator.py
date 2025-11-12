from game.word_validator import WordValidator

def test_valid_four_letter_word():
    validator = WordValidator()
    assert validator.is_valid_word("test") == True