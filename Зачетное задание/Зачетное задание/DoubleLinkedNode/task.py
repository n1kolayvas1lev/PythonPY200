from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка.
    :param value: Любое значение, которое помещено в узел
    :param next_: следующий узел, если он есть, иначе None.
    """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = next_

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return f"Node({self.value}, ({self.next}))" if self.next is None else f"Node({self.value}, (Node{self.next}))"

    def is_valid(self, node: Any):
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional['Node']):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    """
    Класс двойного связного списка, наследованный от Node.
    :param value: Любое значение, которое помещено в узел
    :param _next: следующий узел, если он есть, иначе None.
    :param prev: предыдущий узел, если он есть, иначе None.
    """
    def __init__(self, value: Any, prev: Optional['DoubleLinkedNode'] = None,
                 _next: Optional['DoubleLinkedNode'] = None):
        super().__init__(value=value, next_=_next)
        self.prev = prev

    def __repr__(self) -> str:
        return f'DoubleLinkedNode({self.value},prev {self.prev}, next {self.next})'

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), DoubleLinkedNode)):
            raise TypeError

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional['DoubleLinkedNode']):
        self.is_valid(prev)
        self._prev = prev


if __name__ == "__main__":
    node1 = DoubleLinkedNode(1)
    node2 = DoubleLinkedNode(2)
    node3 = DoubleLinkedNode(3)
    # node1 = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)

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
