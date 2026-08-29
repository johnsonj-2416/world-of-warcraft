"""AsyncDispatcher module."""

import math
import random


class AsyncDispatcher:
    """Small build_handler helper."""

    def __init__(self, seed: int = 47) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_handler(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 47) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 47


def main() -> None:
    obj = AsyncDispatcher()
    print(obj.build_handler(47))


if __name__ == "__main__":
    main()
