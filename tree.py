from typing import Optional, Set, Callable

"""
A basic Tree Node class:
Any data can be put on the node simply by adding kwargs to the init call
"""
class Node:

    def __init__(self, parent: Optional['Node']=None, children: Optional[Set]=None, **kwargs):

        self.children = children if children is not None else set()
        self.parent = parent

        if parent is not None:
            self.parent.children.add(self)

        for name, value in kwargs.items():
            if not hasattr(self, name):
                setattr(self, name, value)

    @property
    def level(self):

        level = 0
        node = self
        while node.parent is not None:
            level += 1
            node = node.parent

        return level

"""
Iterate over the tree structure with pre-order strategy:
first the root, then all it's children
"""
class PreOrderIter:

    def __init__(self, root_node: Node, filter: Callable=None):
        self.root_node = root_node
        self.current_node = root_node

        self.filter = filter

        self.iterated = set()

    def __iter__(self):
        self.current_node = self.root_node
        self.iterated = set()

        return self

    def __next__(self):

        if self.current_node is None:
            raise StopIteration

        result = self.current_node

        next = None
        source_node = self.current_node
        while source_node is not None and next is None:

            # add the first child node that we have not returned yet
            for child_node in source_node.children.difference(self.iterated):

                next = child_node
                self.iterated.add(child_node)
                break

            # if we have found nothing yet, check one level higher. But never go higher than the root node
            if next is None and source_node != self.root_node:
                source_node = source_node.parent
            else:
                source_node = None

        # prepare for the next round
        self.current_node = next

        # skip entries don't pass the filter
        if self.filter is None or self.filter(result):
            return result
        else:
            return self.__next__()
