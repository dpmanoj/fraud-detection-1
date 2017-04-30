import unittest
from common.utils import Graph, DuplicateNodeError


class TestGraphMethods(unittest.TestCase):

    def setUp(self):
        self.__graph = Graph()

    def test_structure(self):
        self.assertIsInstance(self.__graph, Graph)

    def test_add_node(self):
        self.assertEqual(len(self.__graph.get_all_node()), 0)
        self.assertNotEqual(len(self.__graph.get_all_node()), 1)

        self.__graph.add_node(node=1)

        self.assertNotEqual(len(self.__graph.get_all_node()), 0)
        self.assertEqual(len(self.__graph.get_all_node()), 1)

    def test_add_edges(self):

        # Adding nodes
        self.__graph.add_node(node='B')
        self.__graph.add_node(node='A')

        # Connecting two nodes
        self.__graph.add_edge(edge=('A', 'B'))

        # Adding nodes
        self.__graph.add_node(node='C')
        self.__graph.add_node(node='D')

        self.__graph.add_edge(edge=('A', 'D'))

        # Assertions
        self.assertTrue(self.__graph.is_connected('A', 'B'))
        self.assertTrue(self.__graph.is_connected('B', 'A'))
        self.assertFalse(self.__graph.is_connected('C', 'D'))
        self.assertFalse(self.__graph.is_connected('B', 'D'))

    def test_if_two_nodes_was_on_the_same_network(self):

        # Adding nodes
        self.__graph.add_node(node='C')
        self.__graph.add_node(node='D')
        self.__graph.add_node(node='A')
        self.__graph.add_node(node='B')

        self.__graph.add_edge(edge=('A', 'D'))

        # Assertions
        self.assertFalse(self.__graph.same_network(('A', 'B')))
        self.assertFalse(self.__graph.same_network(('B', 'A')))
        self.assertFalse(self.__graph.same_network(('C', 'D')))
        self.assertFalse(self.__graph.same_network(('B', 'D')))
        self.assertTrue(self.__graph.same_network(('A', 'D')))
        self.assertTrue(self.__graph.same_network(('D', 'A')))

    def test_if_node_already_was_on_graph(self):

        # Adding nodes
        self.__graph.add_node(node='C')
        with self.assertRaises(DuplicateNodeError):
            self.__graph.add_node(node='C')


if __name__ == '__main__':
    unittest.main()
