from dataclasses import dataclass
from heap import MaxHeap

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0


class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.max_beehives = max_beehives
        self.beehives = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        self.beehives = MaxHeap(self.max_beehives)
        for hive in hive_list:
            self.beehives.add(hive)
    
    def add_beehive(self, hive: Beehive):
        if len(self.beehives) < self.max_beehives:
            self.beehives.add(hive)
        else:
            max_hive = self.beehives.get_max()
            if hive.capacity > max_hive.capacity:
                self.beehives.add(hive)
            else:
                self.beehives.add(max_hive)

        """
                
        """


    def harvest_best_beehive(self):
        if len(self.beehives) == 0:
            return 0.0

        best_hive = self.beehives.get_max()
        honey_to_harvest = min(best_hive.capacity, best_hive.volume)
        emeralds = honey_to_harvest * best_hive.nutrient_factor
        best_hive.volume -= honey_to_harvest
        return emeralds
