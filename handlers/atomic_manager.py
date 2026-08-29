"""SharedBuilder module."""

import math
import random


class SharedBuilder:
    """Small decode_processor helper."""

    def __init__(self, seed: int = 57) -> None:
        self._state = seed
        self._items: list[int] = []

    def decode_processor(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 57) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 57


def main() -> None:
    obj = SharedBuilder()
    print(obj.decode_processor(57))


if __name__ == "__main__":
    main()
