from game.game import Game

def game_stores_secret_word():
    game = Game()
    game.set_secret_word("play")
    assert game.secret_word == "play"

def test_rejects_invalid_secret_word():
    game = Game()
    result = game.set_secret_word("c$t")
    assert result == False

def test_accepts_valid_secret_word():
    game = Game()
    result = game.set_secret_word("word")
    assert result == True

def test_check_guess_returns_number_of_correct_letters():
    game = Game()
    game.set_secret_word("game")
    result = game.check_guess("gale")
    assert result == 3  # 'g', 'a', and 'e' are

def test_check_guess_no_correct_letters():
    game = Game()
    game.set_secret_word("test")
    result = game.check_guess("abcd")
    assert result == False