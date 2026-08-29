"""SharedService module."""

import math
import random


class SharedService:
    """Small handle_processor helper."""

    def __init__(self, seed: int = 40) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_processor(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 40) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 40


def main() -> None:
    obj = SharedService()
    print(obj.handle_processor(40))


if __name__ == "__main__":
    main()
