import pytest
from elementary.first_word import first_word


def test_first_word():
    assert first_word('Hello World') == 'Hello'
    assert first_word('greetings, friends') == 'greetings'
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
