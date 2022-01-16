class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(self, year: int):
        """Проверяет, является ли год високосным"""
        ...  #
        if year/400 == 0 or year/4 == 0 and year/100 != 0:
            return True
        else:
            return False

    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        ...  #
        if month in [4, 6, 9, 11]:
            return 30
        elif month not in [2, 4, 6, 9, 11]:
            return 31
        elif month == 2 and self.is_leap_year(year):
            return 29
        else:
            return 28

    @staticmethod
    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        ...  #
        if day <= self.get_max_day(month, year):
            return True
        else:
            return False


if __name__ == "__main__":
    date = Date(10, 11, 2020)
    print(date.get_max_day())
    # Write your solution here
    pass
