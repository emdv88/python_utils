from typing import Optional, Set


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
            setattr(self, name, value)

"""
Iterate over the tree structure with pre-order strategy:
first the root, then all it's children
"""
class PreOrderIter:

    def __init__(self, root_node: Node):
        self.root_node = root_node
        self.current_node = root_node

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

        self.current_node = next
        return result
