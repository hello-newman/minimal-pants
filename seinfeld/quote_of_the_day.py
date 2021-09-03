from __future__ import annotations

import random

_QUOTES = [
    "What do you need it for after you read it",
    "How come people don’t have dip for dinner",
    "You have the chicken, the hen, and the rooster",
    "Jerry, just remember, it’s not a lie if you believe it.",
    "Moles — freckles’ ugly cousin",
    "Just remember, when you control the mail, you control… information",
    "Human, it’s human to be moved by a fragrance.",
    "Women don’t respect salad eaters.",
    "Maybe the dingo ate your baby!",
    "People on dates shouldn’t even be allowed out in public.",
    "Three squares? You can’t spare three squares?",
    "He stopped short? ",
]


class Quotes:
    @classmethod
    def create(cls):
        return cls(quotes=_QUOTES)

    def __init__(self, quotes: list[str]) -> None:
        self._quotes = quotes

    def quote(self) -> str:
        return random.choice(self._quotes)
