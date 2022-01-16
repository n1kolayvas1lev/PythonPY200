from driver import Driver

class DriverTypeError(Exception):
    pass

class EngineIsNotRunning(Exception):
    pass

class DriverNotFound(Exception):
    pass


class Car:
    brand = None
    _max_speed = 180
    __created_car = 0

    def __init__(self, color, body_type, model_name, engine_type, gear_type,
                 complectation):
        self.__model_name = model_name
        self.__body_type = body_type
        self._engine_type = engine_type
        self._gear_type = gear_type
        self.complectation = complectation
        self.color = color

        self.__mileage = 0
        self.__driver = None
        self.__engine_status = False

    def __new__(cls, *args, **kwargs):
        cls.__append_new_car_counter()
        print(f'{cls.__created_car} class {cls.__name__} cars created')
        return super().__new__(cls)

    #Методы класса.
    @classmethod
    def change_brand(cls, new_brand: str):
        cls.brand = new_brand

    @classmethod
    def _change_max_speed(cls, max_speed):
        if not isinstance(max_speed, (int, float)):
            raise TypeError(f'{int} or {float} expected, {type(max_speed)} instead')
        cls._max_speed = max_speed

    @classmethod
    def __append_new_car_counter(cls):
        cls.__created_car += 1

    #Статические методы.


    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver: Driver):
        if not isinstance(driver, Driver):
            raise DriverTypeError(f'Used to be {type(Driver)}, instead{type(driver)}')
        self.__driver = driver

# Блок отработки движения.
    def start_engine(self):
        self.__engine_status = True

    def __check_driver(self):
        if self.driver is not None:
            return True
        return False

    def __ready_status(self):
        if not self.__engine_status:
            raise EngineIsNotRunning('Engine is not started.')
        if not self.__check_driver():
            raise DriverNotFound('Driver not found.')
        return True
        # if self.__engine_status and self.__check_driver():
        #     return True
        # return False

    def move(self, distance=10):
        try:
            if self.__ready_status():
                for i in range(distance):
                    print(f'Car moved {i+1} km.')
                print('Done.')
            print('Car is not ready.')
        except (EngineIsNotRunning, DriverNotFound) as e:
            print(repr(e))
# /Блок отработки движения.

# Блок работы с защищёнными методами.
    @property
    def _mileage(self):
        return self.__mileage

    @_mileage.setter
    def _mileage(self, mileage):
        if not isinstance(mileage, (int, float)):
            raise TypeError(f'{int} or {float} expected, {type(mileage)} instead')
        self.__mileage = mileage
# /Блок работы с защищёнными методами.






# Эквивалент @property
    # def set_driver(self, driver: Driver):
    #     if not isinstance(driver, Driver):
    #         return DriverTypeError(f'Used to be {type(Driver)}, instead{type(driver)}')
    #     self.__driver = driver
    #
    # def get_driver(self):
    #     return self.__driver





if __name__ == '__main__':
    print(Car.change_brand('Nissan'))

    car = Car("yellow", 'sedan', 'model', 'benz', 'auto', 'luxe')
    car2 = Car("yellow", 'sedan', 'model', 'benz', 'auto', 'luxe')

    print(car.brand)
    print(car2.brand)

    # Блок отработки движения.
    # car.start_engine()
    # car.driver = Driver('Vasya')
    # car.move()
    # /Блок отработки движения.


# Эквивалент property
    # car.set_driver(Driver('Andrew'))
    # car.get_driver()
    # print(car.get_driver())
#Блок отработки свойств
    # car.driver = Driver('Andrew')
    # print(car.driver)
