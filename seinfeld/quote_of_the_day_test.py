from seinfeld.quote_of_the_day import Quotes


def test_quote() -> None:
    qotd = Quotes.create()
    quote = qotd.quote()
    assert isinstance(quote, str)
    assert len(quote) > 10
