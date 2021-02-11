#!/usr/bin/env python

class TestSomeStuff():  # test case
    def test_two_plus_two_equals_four():  # <1>
        assert 2 + 2 == 4   #  <2>

    def test_three_cubed_is_twenty_seven():
        assert 3 ** 3 == 27

    def test_len_of_spam_is_four():
        word = "spam"
        assert len(word) == 4