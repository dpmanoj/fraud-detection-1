import json

from django.test import TestCase, Client

from utils import Graph


class TestGraphMethods(TestCase):

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

        with self.assertRaises(TypeError):
            self.__graph.add_edge(edge=('Z', 'F'))

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


class TestGraphEndPoints(TestCase):

    def setUp(self):
        self.__client = Client()

    def test_detect_collision(self):
        data = dict(node1=1, node2=2)
        response = self.__client.post(path='/api/v1/graph/collision/',
                                      data=json.dumps(data),
                                      content_type='application/json')

        self.assertEqual(response.status_code, 201)
        obj = json.loads(response.content)
        self.assertTrue(obj.get('is_same_network'))

    def test_create_collision(self):
        data = dict(node1=1, node2=15)
        response = self.__client.post(path='/api/v1/graph/node/collision/',
                                      data=json.dumps(data),
                                      content_type='application/json')

        self.assertEqual(response.status_code, 201)
        obj = json.loads(response.content)
        self.assertEqual(obj.get('message'), "Resource created with successful")
        self.assertEqual(obj.get('edge'), [1, 15])

    def test_if_resource_already_exist(self):
        data = dict(node1=1, node2=2)
        response = self.__client.post(path='/api/v1/graph/node/collision/',
                                      data=json.dumps(data),
                                      content_type='application/json')

        self.assertEqual(response.status_code, 409)
        obj = json.loads(response.content)
        self.assertEqual(obj.get('message'), "Resource already exist")
