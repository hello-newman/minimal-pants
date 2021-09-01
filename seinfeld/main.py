from __future__ import annotations

from colors import blue

from seinfeld.quote_of_the_day import Quotes


def quote_seinfeld() -> None:
    qotd = Quotes.create()
    print(blue(qotd.quote()))


if __name__ == "__main__":
    quote_seinfeld()
