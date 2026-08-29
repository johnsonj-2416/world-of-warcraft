"""SmartRegistry module."""

import math
import random


class SmartRegistry:
    """Small build_session helper."""

    def __init__(self, seed: int = 27) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_session(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 27) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 27


def main() -> None:
    obj = SmartRegistry()
    print(obj.build_session(27))


if __name__ == "__main__":
    main()
