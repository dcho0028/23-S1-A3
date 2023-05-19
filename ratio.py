from __future__ import annotations

import math
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.points = []
    
    def add_point(self, item: T):
        self.points.append(item)
        #self.points.sort()
    
    def remove_point(self, item: T):
        if item in self.points:
            self.points.remove(item)

    def ratio(self, x, y):
        n = len(self.points)
        x_count = max(0, math.ceil(x * n / 100))
        y_count = max(1, math.ceil(y * n / 100))
        sorted_points = self.quicksort(self.points)
        return sorted_points[x_count:-y_count]



    #since sort and sorted are not allowed i made a simple quicksort
    # however base on this ed discussion https://edstem.org/au/courses/10179/discussion/1376885
    # it seems that i can make my own sort and then implement it so i decided to use quickort
    def quicksort(self,arr:[]):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self.quicksort(left) + middle + self.quicksort(right)

if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
