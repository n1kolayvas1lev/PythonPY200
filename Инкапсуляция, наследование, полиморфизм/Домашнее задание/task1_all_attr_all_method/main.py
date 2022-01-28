import random


class Anhuman(Exception):
    pass


class Parent:
    clothes = None
    _height = None
    __legs = None
    __mutant_value = random.randint(0, 999)

    def __init__(self, underwear: str, second_chromosome: str, amount_of_teeth: int):
        self.underwear = underwear
        self._second_chromosome = second_chromosome
        self.__amount_of_teeth = amount_of_teeth
        if self.__amount_of_teeth > 32:
            raise ValueError("Humans can not have > 32 teeth.")
        if not isinstance(self.underwear, str):
            raise TypeError('Pants value must be string.')
        # if self._second_chromosome is not 'y' or 'x':
        #     raise Anhuman('BURN IT!!!!1111111')

    @classmethod
    def change_clothes(cls, clothes: str):
        if not isinstance(clothes, str):
            raise TypeError("Clothes value must be string.")
        cls.clothes = clothes

    @classmethod
    def _change_height(cls, height: (int, float)):
        if not isinstance(height, (int, float)):
            raise TypeError("Height value must be integer or float.")
        cls._height = height

    @classmethod
    def __mutations(cls):
        if cls.__mutant_value >= 500:
            cls.__legs = random.randint(1, 5)
        else:
            cls.__legs = 2

    @classmethod
    def details(cls):
        print(f'Height {cls._height}, Clothes {cls.clothes}, legs {cls.__legs}')

    def __repr__(self):
        return f"{self.underwear}, {self.second_chromosome}, {self.__amount_of_teeth}"

    def __str__(self):
        if self._second_chromosome == 'y':
            return f'Human (male, {self.underwear}, {self.__amount_of_teeth})'
        return f'Human (female, {self.underwear}, {self.__amount_of_teeth})'

    def check_underwear(self):
        print(f'Dirty {self.underwear}.')

    @property
    def second_chromosome(self):
        return self._second_chromosome

    @second_chromosome.setter
    def second_chromosome(self, second_chromosome: str):
        if not isinstance(self._second_chromosome, str):
            raise TypeError("Chromosome type must be string!")
        if self._second_chromosome is not 'y' or 'x':
            raise ValueError("Chromosome must be 'x' if female or 'y' if male.")
        self._second_chromosome = second_chromosome

    @property
    def dentist(self):
        return self.__amount_of_teeth

    @dentist.setter
    def dentist(self, teeth: int):
        if not isinstance(teeth, int):
            raise TypeError("You can not delete !int teeth.")
        if self.__amount_of_teeth + teeth > 32:
            raise ValueError("Humans can not have more than 32 teeth.")
        if self.__amount_of_teeth < teeth:
            raise ValueError("You can not delete more teeth than you have.")
        self.__amount_of_teeth -= teeth

    @staticmethod
    def hello():
        print('Hello!')

    @staticmethod
    def _create_human():
        sex = random.choice(['x', 'y'])
        human = Child('naked', sex, 0)
        return human

    @staticmethod
    def __immaculate_conception():
        adam = Parent('Pants', 'y', 32)
        return adam


class Child(Parent):
    def __init__(self, underwear: str, second_chromosome: str, amount_of_teeth: int):
        super().__init__(underwear=underwear, second_chromosome=second_chromosome, amount_of_teeth=amount_of_teeth)


if __name__ == "__main__":
    dimon = Child("pants", 'y', 13)
    vera = Child("None", 'x', 32)
    vasya = Child("bikini", 'y', 30)
    vika = Child("123", 'x', 0)
    print(dimon)
    print(vera)
    print(vasya)
    print(vika)
    dimon.check_underwear()
    vera.check_underwear()
    vasya.check_underwear()
    vika.check_underwear()
    dimon.details()
    vera.details()
    vasya.details()
    vika.details()


