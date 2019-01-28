
def test_ehlo(example_connection):
    token1, token2 = example_connection
    assert token1 == 'Hello'
    assert token2 == 'World'

