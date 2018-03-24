# test_rps.py

import rps
import pytest
import subprocess
import sys


def test_rock_is_valid_play():
    assert rps.is_valid_play('rock') is True

def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True

def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True

def test_lizard_is_invalid_play():
    assert rps.is_valid_play("lizard") is False

def test_spock_is_invalid_play():
    assert rps.is_valid_play('spock') is False

def test_random_play_is_valid():

    for _ in range(100):
        play = rps.random_play()
        assert rps.is_valid_play(play)
def test_random_play_is_fairish():
    """This test relies on some kind of fairness in the randomness.
    That is of course not 100% accurate, but should work anyway."""
    # spoléha na nahodnost
    plays = [rps.random_play() for _ in range(1000)]
    assert plays.count("rock") > 100
    assert plays.count("paper") > 100
    assert plays.count("scissors") > 100

def test_paper_beats_rock():
    assert rps.determine_game_result("paper", "rock") == 'Vyhrals!'

def test_paper_beats_paper():
    assert rps.determine_game_result("paper", "paper") == 'nerozhodne'

def test_paper_beats_scissors():
    assert rps.determine_game_result("paper", "scissors") == 'Prohrals!'

def test_rock_beats_rock():
    assert rps.determine_game_result("rock", "rock") == 'nerozhodne'

def test_rock_beats_paper():
    assert rps.determine_game_result("rock", "paper") == 'Prohrals!'

def test_rock_beats_scissors():
    assert rps.determine_game_result("rock", "scissors") == 'Vyhrals!'

def input_fake(fake):
    def input_fake_(prompt):
        print(prompt)
        return fake
    return input_fake_
# dekorator:
@pytest.mark.parametrize('play', ["rock", "paper", "scissors"])
def test_whole_game(capsys, play):
    # def test_whole_game(capsys, monkeypatch):
    #monkeypatch.setattr("builtins.input", input_fake_rock)
    rps.main(input=input_fake(play))
    # získaní výstupu při spravném průchodu:
    # captured = capsys.readouterr()
    # assert 'haha' in captured.out
    # i pro starou verzi Pythonu:
    # out, err = capsys.readouterr()
    # assert "haha" in out

    out, err = capsys.readouterr()
    assert "rock, paper or scissors?" in out
    assert ("Prohrals!" in out or
            "Vyhrals!" in out or
            "nerozhodne" in out)
def test_in_subprocess():
    # místo python je lepší použít sys.executable
    # asdf - simuilace zadaní uživatele
    cp = subprocess.run([sys.executable, "rps.py"],
                        input= "asdf\nrock",
                        encoding = "cp1250",
                        stdout = subprocess.PIPE)
    assert cp.stdout.count('rock, paper or scissors?') == 2

# (venv) $ python -m pytest -v test_rps.py
