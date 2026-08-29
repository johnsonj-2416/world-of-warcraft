"""StreamWorker module."""

import math
import random


class StreamWorker:
    """Small decode_worker helper."""

    def __init__(self, seed: int = 91) -> None:
        self._state = seed
        self._items: list[int] = []

    def decode_worker(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 91) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 91


def main() -> None:
    obj = StreamWorker()
    print(obj.decode_worker(91))


if __name__ == "__main__":
    main()
