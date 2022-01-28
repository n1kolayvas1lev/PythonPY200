class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    #какой декоратор следует применить?
    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        # записать условие проверки високосного года
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        #вернуть количество дней указанного месяца
        if month in [4, 6, 9, 11]:
            return 30
        elif month not in [2, 4, 6, 9, 11]:
            return 31
        elif month == 2 and self.is_leap_year(year):
            return 29
        else:
            return 28

    def is_valid_date(self, day: int, month: int, year: int) -> bool:
        """Проверяет, является ли дата корректной"""
        #если указанный набор день, месяц и год неверны, то вызвать ошибку ValueError
        if 0 < day <= self.get_max_day(month, year) or 0 > month > 12 or 0 > year:
            return True
        else:
            return False

    #записать getter и setter для дня
    @property
    def day(self):
        return self.day

    @day.setter
    def day(self, day: int):
        if not isinstance(day, int):
            raise ValueError("Day must be int.")
        if self.is_valid_date(day, self.month, self.year):
            self.day = day
        else:
            raise ValueError("Day is not correct.")


    #записать getter и setter для месяца

    @property
    def month(self):
        return self.month

    @month.setter
    def month(self, month: int):
        if not isinstance(month, int):
            raise ValueError("Month must be int.")
        if self.is_valid_date(self.day, month, self.year):
            self.month = month
        else:
            raise ValueError("Month is not correct.")
    #записать getter и setter для года


if __name__ == "__main__":
    ...
