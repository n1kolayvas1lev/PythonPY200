
class Date:
    def __init__(self, day: int, month: int, year: int):
        if not isinstance(day, int):
            raise TypeError
        if day > 31 or month > 12:
            raise ValueError
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"Date({self.day}.{self.month}.{self.year})"

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
if __name__ == "__main__":
    date = Date(22, 11, 2015)
    print(date)
