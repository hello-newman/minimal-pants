from colors import blue

from seinfeld.quote_of_the_day import Quotes


def quoute_seinfeld() -> None:
    qotd = Quotes.create()
    print(blue(qotd.quote()))


if __name__ == "__main__":
    quoute_seinfeld()
