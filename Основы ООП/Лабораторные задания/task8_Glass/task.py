from typing import Union


class Glass:

    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.occupied_volume = None
        self.set_cap_vol(capacity_volume)
        self.set_occ_vol(capacity_volume, occupied_volume)

    def set_cap_vol(self, capacity_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume < 0:
            raise ValueError
        self.capacity_volume = capacity_volume

    def set_occ_vol(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if capacity_volume < occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume

    def add_water(self, a_water: Union[int, float]):
        if not isinstance(a_water, (int, float)):
            raise TypeError
        if a_water < 0:
            raise ValueError
        if a_water + self.occupied_volume > self.capacity_volume:
            raise ValueError
        self.occupied_volume += a_water

    def remove_water(self, r_water: Union[int, float]):
        if not isinstance(r_water, (int, float)):
            raise ValueError
        if r_water < 0:
            raise ValueError
        if self.occupied_volume - r_water < 0:
            raise ValueError
        self.occupied_volume -= r_water


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
    glass.add_water(50)
    print(glass.capacity_volume, glass.occupied_volume)
    glass.remove_water(55)
    print(glass.capacity_volume, glass.occupied_volume)



#Добавить методы add_water и remove_water
