from flask_restful import Resource, reqparse

from common.utils import UtilsService, Graph


class NodeDetail(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('node1', type=int, required=True, location=['args', 'json'])
        self.reqparse.add_argument('node2', type=int, required=True, location=['args', 'json'])
        super(NodeDetail, self).__init__()

    def get(self, id):
        return {'hello': 'Details'}

    def post(self, **kwargs):
        args = self.reqparse.parse_args()
        node_1 = args.get('node1')
        node_2 = args.get('node2')

        g = Graph()

        # Loading Graph
        g = UtilsService.load_graph(UtilsService.FIXTURE_DIRS + "/collisions.data")
        # g.add_node(nodes=[node_1, node_2])
        g.add_edge(edge=(node_1, node_2))

        UtilsService.store_graph(UtilsService.FIXTURE_DIRS + "/collisions.data", (node_1, node_2))

        print g

        return "Ok", 201


class NodeCollision(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('node1', type=int, required=True, location=['args', 'json'])
        self.reqparse.add_argument('node2', type=int, required=True, location=['args', 'json'])
        super(NodeCollision, self).__init__()

    def get(self, id):
        args = self.reqparse.parse_args()
        print args
        return "Ok", 200

    def post(self, **kwargs):
        args = self.reqparse.parse_args()
        node_1 = args.get('node1')
        node_2 = args.get('node2')

        g = Graph()

        # Loading Graph
        g = UtilsService.load_graph(UtilsService.FIXTURE_DIRS + "/collisions.data")
        result = g.same_network((node_1, node_2))

        return dict(is_same_network=result), 201


class NodeList(Resource):
    def get(self):
        return {'hello': 'world'}