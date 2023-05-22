from __future__ import annotations

import math
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        """
        empty array self.points
        """
        self.points = []
    
    def add_point(self, item: T):
        """
        append the item into the self.points list
        """
        self.points.append(item)

    
    def remove_point(self, item: T):
        """
        remove the item in the list self.points
        """
        if item in self.points:
            self.points.remove(item)

    def ratio(self, x, y):
        """
        doc: having the ratio of the list to be extracted . by that we use the n as the len of table
        then the x and y count is used with function max to picked out the max value of 0,x*n percentage
        and max value of y*n percentage . then it will go through the quicksort made base on the units
        we have learned and then it will grab the elements in between of the index given .

        """
        n = len(self.points)
        x_count = max(0, math.ceil(x * n / 100))
        y_count = max(1, math.ceil(y * n / 100))
        sorted_points = self.quicksort(self.points)
        return sorted_points[x_count:-y_count]



    #since sort and sorted are not allowed i made a simple quicksort
    # however base on this ed discussion https://edstem.org/au/courses/10179/discussion/1376885
    # it seems that i can make my own sort and then implement it so i decided to use quickort
    def quicksort(self,arr:[]):

        """
        This is a simple quicksort build to sort the elements in the list using a pivot

        Doc: this quicksort have a base cae of len(arr) leeser equlas to 1
        it will return the list array . it will first get the pivot of the middle
        part of the list and then it takes the left and then the right side of the
        list left for elements smaller than the pivot and right for elements larger
         than the pivot and the middle it takes the pivot . then it will perform the
         recursive calls with the middle array to form the sorted array .

         time complexity

         best case: O(n log n) where n is the number of the elements in the
         array and the log n is cause by the list splitting in half. as the steps reduced
         the problem size by half

         worst case: O(n**2) where the partioning is unbalanced as the pivot element
         consistently selects the largest or the smallest element in the array .
         


        """
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
