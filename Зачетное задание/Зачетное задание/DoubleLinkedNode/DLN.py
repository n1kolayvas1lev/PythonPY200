from typing import Any, Optional

from task import Node


class DoubleLinkedNode(Node):
    """
    Класс двойного связного списка, наследованный от Node.
    :param value: Любое значение, которое помещено в узел
    :param next_: следующий узел, если он есть, иначе None.
    :param prev: предыдущий узел, если он есть, иначе None.
    """
    def __init__(self, value: Any, prev: Optional['DoubleLinkedNode'] = None,
                 next_: Optional['DoubleLinkedNode'] = None):
        super().__init__(value=value, next_=next_)
        self.prev = prev

    def __repr__(self) -> str:
        return f'DoubleLinkedNode({self.value},{self.prev}, {self.next})'

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), DoubleLinkedNode)):
            raise TypeError

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional['DoubleLinkedNode'] = None):
        self.is_valid(prev)
        self._prev = prev


if __name__ == "__main__":
    node1 = DoubleLinkedNode(1)
    node2 = DoubleLinkedNode(2)
    node3 = DoubleLinkedNode(3)
    # node2.prev(node1)
    # node3.prev(node2)
    # node1.next(node2)
    # node2.next(node3)
    print(repr(node1))
    print(repr(node2))
    print(repr(node3))
    node1.next = node2
    node2.next = node3

    node2.prev = node1
    node3.prev = node2
    print(repr(node1))
    print(repr(node2))
    print(repr(node3))
    print(type(node1))
    print(type(node2))
    print(type(node3))
