import unittest

from tree import PreOrderIter, Node


class TestTree(unittest.TestCase):

    def test_pre_order_iterator(self):
        f = Node(name="f")
        b = Node(name="b", parent=f)
        a = Node(name="a", parent=b)
        d = Node(name="d", parent=b)
        c = Node(name="c", parent=d)
        e = Node(name="e", parent=d)
        g = Node(name="g", parent=f)
        i = Node(name="i", parent=g)
        h = Node(name="h", parent=i)

        result_list = [node.name for node in PreOrderIter(f)]

        possible_results = [
            ['f', 'b', 'a', 'd', 'c', 'e', 'g', 'i', 'h'],
            ['f', 'b', 'a', 'd', 'e', 'c', 'g', 'i', 'h'],
            ['f', 'b', 'd', 'c', 'e', 'a', 'g', 'i', 'h'],
            ['f', 'b', 'd', 'e', 'c', 'a', 'g', 'i', 'h'],
            ['f', 'g', 'i', 'h', 'b', 'a', 'd', 'c', 'e'],
            ['f', 'g', 'i', 'h', 'b', 'a', 'd', 'e', 'c'],
            ['f', 'g', 'i', 'h', 'b', 'd', 'c', 'e', 'a'],
            ['f', 'g', 'i', 'h', 'b', 'd', 'e', 'c', 'a'],
        ]

        found = False
        for expected_result in possible_results:
            try:
                self.assertListEqual(result_list, expected_result)
                found = True
            except AssertionError:
                pass

        self.assertTrue(found)