from pure_rummy import rummy


def test_input_invalid_none():
    result =  rummy(None)
    assert result == 'Sorry, that is invalid'

def test_input_invalid_empty_string():
    result =  rummy('')
    assert result == 'Sorry, that is invalid'

def test_input_invalid_integer():
    result =  rummy(5)
    assert result == 'Sorry, that is invalid'