import pytest
from carddeck import CardDeck

@pytest.fixture
def deck():
    return CardDeck("TestUser")

def test_deck_has_52_cards(deck):
    assert len(deck) == 52

def test_drawing_one_card_decrements_len(deck):
    deck.draw()
    assert len(deck) == 51