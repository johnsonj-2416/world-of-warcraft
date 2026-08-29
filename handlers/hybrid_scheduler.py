"""SecureDispatcher module."""

import math
import random


class SecureDispatcher:
    """Small render_adapter helper."""

    def __init__(self, seed: int = 3) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_adapter(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 3) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 3


def main() -> None:
    obj = SecureDispatcher()
    print(obj.render_adapter(3))


if __name__ == "__main__":
    main()
