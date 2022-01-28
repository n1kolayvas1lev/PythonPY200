from collections.abc import MutableSequence

from typing import Any, Iterable, Optional

from node import Node


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        self._head: Optional[Node] = None
        self._tail = self._head
        self._len = 0
        if data is not None:
            for value in data:
                self.append(value)

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self._len:  # для for
            raise IndexError()

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def __len__(self):
        return len(self)

    def __getitem__(self, item: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(item)
        return node.value

    def __setitem__(self, item: int, value: Any):
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(item)
        node.value = value

    def __delitem__(self, key: int) -> None:
        """
        Метод удаляет значение узла по данному индексу.
        :param key: индекс
        :return: None
        """
        if not isinstance(key, int):
            raise TypeError("Ключ для удаления должен быть целочисленным значением.")
        del self[key]
        self._len -= 1

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
            self.append(Node(value))
        if index == 0:
            self._head = Node(value)
            for _ in range(self._len):
                self.linked_nodes(self._head, self[_])
            self._len += 1
        else:
            insert_node = Node(value)
            self.linked_nodes(self[index - 1], insert_node)
            for _ in range(index+1, self._len):
                self.linked_nodes(self[index], self[_])
            self._len += 1

    def append(self, value: Any) -> None:
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def __iter__(self):
        return self


# class DoubleLinkedList(LinkedList):
#     ...


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
