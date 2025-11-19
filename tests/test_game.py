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