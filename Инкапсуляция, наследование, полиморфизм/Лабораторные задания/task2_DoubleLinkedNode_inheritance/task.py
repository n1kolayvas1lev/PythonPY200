from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_

# реализовать класс DoubleLinkedNode


class DoubleLinkedNode(Node):

    def __init__(self, value: Any, next_: Optional["DoubleLinkedNode"] = None,
                 prev: Optional["DoubleLinkedNode"] = None):
        super().__init__(value=value, next_=next_)
        self.prev = prev

    def __repr__(self):
        if self.next and self.prev is None:
            return f"DoubleLinkedNode({self.value}, {None}, {None})"
        if self.next is None:
            return f"DoubleLinkedNode({self.value}, DoubleLinkedNode({self.prev}), {None})"
        if self.prev is None:
            return f"DoubleLinkedNode({self.value}, {None}, DoubleLinkedNode({self.next}))"
        else:
            return f"DoubleLinkedNode({self.value}, DoubleLinkedNode({self.prev}), DoubleLinkedNode({self.next}))"

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), DoubleLinkedNode)):
            raise TypeError

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["DoubleLinkedNode"]):
        self.is_valid(prev)
        self._prev = prev
