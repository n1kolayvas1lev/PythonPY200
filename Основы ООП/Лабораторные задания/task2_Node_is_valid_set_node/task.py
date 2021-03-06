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

        self.next = None
        self.set_next(next_) #установить значение следующего узла с помощью метода set_next

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError
        #метод проверки корректности связываемого узла

    def set_next(self, next_: Optional["Node"] = None) -> None:
        #  метод должен проверять корректность узла и устанавливать значение атрибуту next
        self.is_valid(next_)
        self.next = next_


if __name__ == '__main__':
    #инициализируйте два узла с любыми значеними
    node1 = Node(1)
    node2 = Node(2)
    #  свяжите первый узел со вторым
    node1.set_next(node2)
    print(node1)
    print(node2)
