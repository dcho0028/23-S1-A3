from __future__ import annotations
from threedeebeetree import Point

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    sorted_points = sorted(my_coordinate_list, key=lambda p: p[0])  # sort the points based on the x-axis

    def _octant_index(point):
        """
        This function returns the octant index of a point that
        represents the region in which the point resides in a space.
        If octant_index > 0, the point is in the positive half of the axis.
        """
        octant_index = 0
        if point[0] > 0:
            octant_index |= 1
        if point[1] > 0:
            octant_index |= 2
        if point[2] > 0:
            octant_index |= 4
        return octant_index

    def ordering_aux(points):
        n = len(points)
        if n <= 2:  # Base case: return the points with its pointers
            return [point for point in points]

        m = n // 2
        left_half = points[:m]
        right_half = points[m:]

        # Recursive case: recursively divide and conquer the two halves of the list
        left_ordered = ordering_aux(left_half)
        right_ordered = ordering_aux(right_half)
        pointers = [[], [], [], [], [], [], [], []]
        for p in left_ordered:
            i = _octant_index(p)
            pointers[i].append(p)
        for p in right_ordered:
            i = _octant_index(p)
            pointers[i].append(p)

        return [point for points in pointers for point in points]

    return ordering_aux(sorted_points)
