"""LocalBuffer module."""

import math
import random


class LocalBuffer:
    """Small sync_context helper."""

    def __init__(self, seed: int = 73) -> None:
        self._state = seed
        self._items: list[int] = []

    def sync_context(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 73) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 73


def main() -> None:
    obj = LocalBuffer()
    print(obj.sync_context(73))


if __name__ == "__main__":
    main()
