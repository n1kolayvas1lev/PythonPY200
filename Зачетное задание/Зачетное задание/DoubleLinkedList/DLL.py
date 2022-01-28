from task import LinkedList

from typing import Any, Iterable, Optional

from node import DoubleLinkedNode


class DoubleLinkedList(LinkedList):
    def __init__(self, data: Iterable = None):
        super().__init__(data=data)
        self._head: Optional[DoubleLinkedNode] = None

    @staticmethod
    def linked_nodes(left_node: Optional[DoubleLinkedNode] = None,
                     right_node: Optional[DoubleLinkedNode] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node
        right_node.prev = left_node

    def insert(self, index: int, value: Any) -> None:
        """
        Функция вставки значения по указанному индексу.
        :param index: int
        :param value: Any
        :return: None
        """
        if not isinstance(index, int):
            raise TypeError("Ключ для вставки должен быть целочисленным значением.")
        if index == self._len:
            self.append(DoubleLinkedNode(value))
        if index == 0:
            self._head = DoubleLinkedNode(value)
            for _ in range(self._len):
                self.linked_nodes(self._head, self[_])
            self._len += 1
        else:
            insert_node = DoubleLinkedNode(value)
            self.linked_nodes(self[index - 1], insert_node)
            for _ in range(index+1, self._len):
                self.linked_nodes(self[index], self[_])
            self._len += 1

    def append(self, value: Any) -> None:
        """ Добавление элемента в конец связного списка. """
        append_node = DoubleLinkedNode(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1


if __name__ == "__main__":
    ll = [1, 2, 3]
    print(ll)
    print(len(ll))
    print(type(ll[1]))

    ll.insert(4, "4_index4")
    print(ll)
    print(len(ll))
    print(type(ll[3]))

    ll.insert(0, "0_index0")
    print(ll)
    print(len(ll))
    print(type(ll[0]))

    ll.insert(1, "1_index1")
    print(ll)
    print(len(ll))
    print(type(ll[1]))

    ll.__delitem__(1)
    print(ll)
