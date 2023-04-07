import pytest
from itertools import product, chain
from card import parse_card

@pytest.mark.parametrize('argument', [
    None,
    0,
    [],
    ['A', 'H'],
    ['A'],
    [3],
    {0: 'A', 1: 'H'},
    '21D',
    '13H',
    '4P',
    '11DD',
    '1D',
    '3HD',
    'CO',
    '01D',
    '05S',
    '4s',
    'fiveS',
    '8c',
    'ah',
    'aS',
    '-1H',
    ';*',
    ('J', 'C'),
    (x for x in 'AS'),
])
def test_parse_card_requires_valid_argument(argument):
    with pytest.raises(ValueError):
        parse_card(argument)

@pytest.mark.parametrize('shorthand, expected_rank', [
    ('5H', '5'),
    ('AD', 'ace'),
    ('10S','10'),
    ('4C', '4'),
    ('JC', 'jack'),
    ('QD', 'queen'),
    ('KH', 'king'),
])
def test_parse_card_parses_rank_basics(shorthand, expected_rank):
    assert parse_card(shorthand)['rank'] == expected_rank

numeric_ranks = list(range(2, 11))
numeric_names = [(str(x), str(x)) for x in numeric_ranks]
face_names = [('A', 'ace'), ('J', 'jack'), ('Q', 'queen'), ('K', 'king')]
all_ranks = list(chain(numeric_names, face_names))
suit_names = [('C', 'clubs'), ('D', 'diamonds'), ('H', 'hearts'), ('S', 'spades')]

def build_case(ranks, suits):
    return ((r[0], r[1], s[0], s[1]) for r, s in product(ranks, suits))

rank_tests = [(f'{r}{s}', f'{rn}') for r, rn, s, _ in build_case(all_ranks, suit_names)]
@pytest.mark.parametrize('shorthand, expected_rank', rank_tests)
def test_parse_card_parses_rank(shorthand, expected_rank):
    assert parse_card(shorthand)['rank'] == expected_rank

suit_tests = [(f'{r}{s}', f'{sn}') for r, _, s, sn in build_case(all_ranks, suit_names)]
@pytest.mark.parametrize('shorthand, expected_suit', suit_tests)
def test_parse_card_parses_suit(shorthand, expected_suit):
    assert parse_card(shorthand)['suit'] == expected_suit

@pytest.mark.parametrize('shorthand, expected_description', [
    ('AS', 'an ace of spades'),
    ('2C', 'a two of clubs'),
    ('3C', 'a three of clubs'),
    ('4D', 'a four of diamonds'),
    ('5S', 'a five of spades'),
    ('6H', 'a six of hearts'),
    ('7C', 'a seven of clubs'),
    ('8D', 'an eight of diamonds'),
    ('9S', 'a nine of spades'),
    ('10H', 'a ten of hearts'),
    ('JD', 'a jack of diamonds'),
    ('QC', 'a queen of clubs'),
    ('KH', 'a king of hearts'),
])
def test_parse_card_description_basics(shorthand, expected_description):
    assert parse_card(shorthand)['description'] == expected_description

nn = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
def convert_rn(rn):
    return nn[int(rn)] if rn.isdigit() else rn
    
description_tests = [(f'{r}{s}', f'{"an" if r in "A8" else "a"} {convert_rn(rn)} of {sn}') for r, rn, s, sn in build_case(all_ranks, suit_names)]
@pytest.mark.parametrize('shorthand, expected_description', description_tests)
def test_parse_card_description_basics(shorthand, expected_description):
    assert parse_card(shorthand)['description'] == expected_description

