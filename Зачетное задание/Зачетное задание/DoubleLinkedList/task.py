from collections import MutableSequence


class LinkedList(MutableSequence):
    def __init__(self):
        ...

    def __repr__(self):
        ...

    def __str__(self):
        ...

    def __len__(self):
        ...

    def __getitem__(self, item):
        ...

    def __setitem__(self, key, value):
        ...

    def __delitem__(self, key):
        ...

    def insert(self, index: int, value: _T) -> None:
        ...

    def append(self, value: _T) -> None:
        ...


class DoubleLinkedList(LinkedList):
    ...


if __name__ == "__main__":
    ...
