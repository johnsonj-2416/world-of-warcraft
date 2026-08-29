"""SecureWorker module."""

import math
import random


class SecureWorker:
    """Small flush_context helper."""

    def __init__(self, seed: int = 79) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_context(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 79) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 79


def main() -> None:
    obj = SecureWorker()
    print(obj.flush_context(79))


if __name__ == "__main__":
    main()
