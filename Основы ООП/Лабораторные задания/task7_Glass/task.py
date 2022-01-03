from typing import Union


#   создать класс Glass
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
    def set_occ_vol(self,capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if capacity_volume < occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
