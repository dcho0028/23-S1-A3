from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:

    key: Point
    item: I
    subtree_size: int = 1
    child_nodes: list[BeeNode | None] = field(default_factory=lambda: [None] * 8)

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        """
        This code uses the child_nodes and what this child nodes represents
        is the child nodes of the current node. it is a list of size 8, initialized with None values.
        With that the get child for key method is based on to retrieve the child
        node based on a given point . it takes the point and then its
        variable is used to determine the octant (child index) based on the coordinates.
        the octant is calculated by comparing the coordinates of the given point with the current node's key.
        Finally, the method returns the child node corresponding to the determined octant from the child_nodes list.

        time complexity O(1) because it performs a constant number of operations
        regardless of the size of the tree or the number of child nodes.
        """
        x,y,z = self.key
        bx,by,bz = point

        octant = 0
        if bx >= x:
            octant += 1
        if by >= y:
            octant += 2
        if bz >= z:
            octant += 4

        return self.child_nodes[octant]



class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    # did by me
    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        """
        Doc :  this code is used to retrieve a tree node with a specific key
        from the Bee Tree data structure it will take the key and search for the node
        It start with the self.root being the current and then it enter a while loop
        if the current isnt none it checks if the current node's key matches the desired key
        if it is , then  it means the node with the desired key has been found, so it returns the current node
        If the keys are not equal, then it calculates the octant value based on the comparisons
        between the coordinates of the key and the current node's key . after that
        the octant value determines the direction to traverse the tree based on the comparisons.
        It helps determine which child node to explore next.
        The method calls current.get_child_for_key(key) to retrieve the child node in the appropriate octant based on the key value

        time complexity:

        best case : o(1) the desired node is found at the root node itself(self.root) as the method
        performs a single comparison to determine if the keys are equal

        worst case: O(log n) where n is the number of the nodes in the tree as it
        needs to traverse the tree from the root to the leaf nodes or until the desired node is found
        """
        current = self.root
        while current is not None:
            if current.key == key:
                return current
            octant = 0
            if key[0] >= current.key[0]:
                octant += 1
            if key[1] >= current.key[1]:
                octant += 2
            if key[2] >= current.key[2]:
                octant += 4
            current = current.get_child_for_key(key)
        raise KeyError(f"Key {key} not in tree.")

    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    #must edit
    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it

        Doc: first this code checks if the current is none if it is then it
        means the tree is empty at that position, so a new node is
        created with the given key and item and returned . whenn it isnt none
        the method determines the octant in which the new node should be inserted.
        It compares the coordinates of the key with the coordinates of the current
        node's key to determine the appropriate octant based on their relative values.
        after that , the method calls current.get_child_for_key(key) to retrieve the
        child node in the determined octant and source it to child . if its none
        then it does the same thing where there is no existing node in that octant
        it will assign as the new node is created with the given key and item
        If the child node exists, the method recursively calls self.insert_aux
        to continue the insertion process on the child node until a suitable position is found.
        After inserting the new node or completing the recursive insertion process, the subtree_size
        of the current node is incremented to account for the newly added node or updated subtree size.

        time complexity:

        best case: O(1) this is when the tree is empty (current is None),
        the given code creates a new node and returns it in constant time.

        worst case: The overall time complexity of the insert_aux method depends on
        the shape and balance of the tree. In balanced trees, such as when using an optimized
        insertion algorithm, the time complexity can be O(log n) on average. In unbalanced trees,
        the time complexity can degrade to O(n) in the worst case.


        """
        if current is None:
            return BeeNode(key, item)

        octant = 0
        if key[0] >= current.key[0]:
            octant += 1
        if key[1] >= current.key[1]:
            octant += 2
        if key[2] >= current.key[2]:
            octant += 4

        child = current.get_child_for_key(key)
        if child is None:
            child = BeeNode(key, item)
            current.child_nodes[octant] = child
        else:
            current.child_nodes[octant] = self.insert_aux(child, key, item)

        current.subtree_size += 1
        return current

    # must edit
    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        for child in current.child_nodes:
            if child is not None:
                return False
        return True


    """
    return all(child is None for child in current.children)
    """
if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
