import unittest

from tree import PreOrderIter, Node


class TestTree(unittest.TestCase):

    def test_node_level(self):
        f = Node(name="f")
        b = Node(name="b", parent=f)
        a = Node(name="a", parent=b)
        d = Node(name="d", parent=b)
        c = Node(name="c", parent=d)
        e = Node(name="e", parent=d)
        g = Node(name="g", parent=f)
        i = Node(name="i", parent=g)
        h = Node(name="h", parent=i)

        self.assertEqual(f.level, 0)
        self.assertEqual(b.level, 1)
        self.assertEqual(a.level, 2)
        self.assertEqual(d.level, 2)
        self.assertEqual(c.level, 3)
        self.assertEqual(e.level, 3)
        self.assertEqual(g.level, 1)
        self.assertEqual(i.level, 2)
        self.assertEqual(h.level, 3)

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

        # since the children are stored in sets, the result my vary
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

        # pass the test if one of the possible results is received
        found = False
        for expected_result in possible_results:
            try:
                self.assertListEqual(result_list, expected_result)
                found = True
            except AssertionError:
                pass

        self.assertTrue(found)


    def test_pre_order_iterator_filter(self):
        f = Node(name="f")
        b = Node(name="b", parent=f)
        a = Node(name="a", parent=b)
        d = Node(name="d", parent=b)
        c = Node(name="c", parent=d)
        e = Node(name="e", parent=d)
        g = Node(name="g", parent=f)
        i = Node(name="i", parent=g)
        h = Node(name="h", parent=i)

        result_list = [node.name for node in PreOrderIter(f, filter=lambda node: node.name == "d")]
        self.assertListEqual(result_list, ['d'])

        result_list = [node.name for node in PreOrderIter(f, filter=lambda node: node.level > 2)]
        result_set = {'c', 'e', 'h'}

        self.assertEqual(len(result_list), len(result_set))
        for node in result_list:
            self.assertIn(node, result_set)