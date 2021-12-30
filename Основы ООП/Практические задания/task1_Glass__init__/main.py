from typing import Union
# Как на лекции.
# Удовлетворяем первое условие.
# class Glass:
#     def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
#
#         if not isinstance(capacity_volume, (int, float)):
#             raise TypeError
#         if not capacity_volume > 0:
#             raise ValueError
#         self.capacity_volume = capacity_volume
#
#         if not isinstance(occupied_volume, (int, float)):
#             raise TypeError
#         if not occupied_volume >= 0:
#             raise ValueError
#         self.occupied_volume = occupied_volume
#
# # Удовлетворяем второе условие.
# if __name__ == "__main__":
#     glass1 = Glass(100, 50)
#     glass2 = Glass(200, '1000') # Третье условие.




class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):

        self.capacity_volume = self.__check_capacity_volume(capacity_volume)
        self.occupied_volume = self.__check_occupied_volume(occupied_volume)

        self.__check_overflow(self.capacity_volume, self.occupied_volume)

    @staticmethod
    def __check_capacity_volume(value: Union[int, float]) -> Union[int, float]:
        # " __ " Делаем метод частным
        if not isinstance(value, (int, float)):
            raise TypeError
        if not value > 0:
            raise ValueError
        return value

    @staticmethod
    def __check_occupied_volume(value):
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError
        return value

    @staticmethod
    def __check_overflow(capacity, occupied):
        if capacity < occupied:
            raise OverflowError('Стакан не резиновый')

if __name__ == "__main__":
    glass1 = Glass(500, 100)
    glass2 = Glass(200, 100)
    glass3 = Glass(200, 300)


# if __name__ == "__main__":
#     ...  # инициализировать два объекта типа Glass
#     glass1 = Glass(500, 100)
#     glass2 = Glass(50, 10)
#     glass3 = Glass(30, 40)
#     #  попробовать инициализировать не корректные объекты
