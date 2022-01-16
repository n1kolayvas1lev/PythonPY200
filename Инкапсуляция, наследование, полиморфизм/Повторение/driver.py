class Driver:
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name})"

    def __str__(self):
        return f"Driver {self.__name}"

if __name__ == '__main__':
    ivan = Driver('Ivan')
    alex = Driver('Alex')

    print(ivan)
    print(alex)