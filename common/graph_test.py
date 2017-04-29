import unittest
from graph import Graph


class TestGraphMethods(unittest.TestCase):

    def setUp(self):
        self.__graph = Graph()

    def test_add_vertex(self):
        self.assertNotEqual(len(self.__graph.get_all_vertex()), 0)
        self.assertEqual(len(self.__graph.get_all_vertex()), 1)

        self.__graph.add_vertex(1)

        self.assertNotEqual(len(self.__graph.get_all_vertex()), 0)
        self.assertEqual(len(self.__graph.get_all_vertex()), 1)

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()
