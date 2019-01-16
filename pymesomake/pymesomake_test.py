from .pymesomake import is_mesoword, is_wingword, Mesoword, Poemline
import pytest


class TestIsMesoword(object):
    def test_reject_first_not_contained(self):
        word   = 'mushroom'
        first  = 'j'
        second = 'o'
        assert is_mesoword(word, first, second) == (False, -1)

    def test_reject_second_is_contained(self):
        word   = 'banjo'
        first  = 'j'
        second = 'o'
        assert is_mesoword(word, first, second) == (False, -1)

    def test_accept_only_first_is_contained(self):
        word   = 'ganja'
        first  = 'j'
        second = 'o'
        assert is_mesoword(word, first, second) == (True, 3)

    def test_accept_only_first_is_contained_at_end(self):
        word   = 'kitaj'
        first  = 'j'
        second = 'o'
        assert is_mesoword(word, first, second) == (True, 4)

    def test_accept_one_character_word(self):
        word   = 'i'
        first  = 'i'
        second = 'n'
        assert is_mesoword(word, first, second) == (True, 0)

    def test_reject_one_character_word(self):
        word   = 'i'
        first  = 'f'
        second = 'i'
        assert is_mesoword(word, first, second) == (False, -1)

    def test_last_character_in_mesostring_accept(self):
        word   = 'mushroom'
        first  = 'o'
        second = ''
        assert is_mesoword(word, first, second) == (True, 5)

    def test_last_character_in_mesostring_reject(self):
        word   = 'mushroom'
        first  = 'j'
        second = ''
        assert is_mesoword(word, first, second) == (False, -1)


class TestIsWingword(object):
    def test_accept_first_contained_second_not_contained(self):
        word   = 'james'
        first  = 'j'
        second = 'o'
        num_first = 0
        assert is_wingword(word, first, second, num_first) is True

    def test_reject_first_contained_second_contained(self):
        word   = 'joyce'
        first  = 'j'
        second = 'o'
        num_first = 0
        assert is_wingword(word, first, second, num_first) is False

    def test_reject_first_contained_second_not_contained_second_occurrence(self):
        word   = 'james'
        first  = 'j'
        second = 'o'
        num_first = 1
        assert is_wingword(word, first, second, num_first) is False

    def test_reject_first_contained_second_contained_second_occurrence(self):
        word   = 'joyce'
        first  = 'j'
        second = 'o'
        num_first = 1
        assert is_wingword(word, first, second, num_first) is False

class TestPoemline(object):
    def test_assemble_mesoword_line(self):
        mesoword = Mesoword('a', 'b', 'prepared', 4, 1, 2)
        poemline = Poemline(mesoword)
        assert poemline.assemble() == 'prepAred'

    def test_assemble_mesoword_line_with_left_wing(self):
        mesoword = Mesoword('a', 'b', 'prepared', 4, 1, 2)
        poemline = Poemline(mesoword)
        poemline.prepend('arbitrary')
        poemline.prepend('barbary')
        assert poemline.assemble() == 'barbary arbitrary prepAred'

    def test_assemble_mesoword_line_with_right_wing(self):
        mesoword = Mesoword('a', 'b', 'prepared', 4, 1, 2)
        poemline = Poemline(mesoword)
        poemline.append('arbitrary')
        poemline.append('barbary')
        assert poemline.assemble() == 'prepAred arbitrary barbary'
