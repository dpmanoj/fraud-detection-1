import json

from flask_restful import Resource, reqparse
from common.utils import UtilsService, Graph, DuplicateEdgeError


class NodeDetail(Resource):

    """
    Insert new collisions in the graph, remember that two collisions are represented 
    by a pair (x, y) that is a edge in graph structure
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('node1', type=int, required=True, location=['args', 'json'])
        self.reqparse.add_argument('node2', type=int, required=True, location=['args', 'json'])
        super(NodeDetail, self).__init__()

    def post(self, **kwargs):

        # Setting default responses
        msg = "Resource created with successful"
        status = 201

        # Get args
        args = self.reqparse.parse_args()
        node_1 = args.get('node1')
        node_2 = args.get('node2')

        # Loading Graph
        g = UtilsService.load_graph(UtilsService.FIXTURE_DIRS + "/collisions.data")

        try:
            # Insert new node, we can adding new nodes directly say what edge, if some of node doesn't
            # exist we'll create
            g.add_node(nodes=[node_1, node_2])
            g.add_edge(edge=(node_1, node_2))

            UtilsService.store_graph(UtilsService.FIXTURE_DIRS + "/collisions.data",
                                     (node_1, node_2))

        except DuplicateEdgeError:
            msg = "Resource already exist"
            status = 409

        return json.dumps({'message': msg, "edge": (node_1, node_2), "status": status}), status


class NodeCollision(Resource):

    """
    Check when two nodes was in the same network collision
    """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('node1', type=int, required=True, location=['args', 'json'])
        self.reqparse.add_argument('node2', type=int, required=True, location=['args', 'json'])
        super(NodeCollision, self).__init__()

    def post(self, **kwargs):

        """
        I chosen make a operation that not represent directly a resource using the POST verb, 
        but this is a open question when we work with restful, I chosen this way because I think that is
        a acceptable way to do and not is a anti-pattern.
        
        :param kwargs: 
        :return: json with result of operation
        """
        args = self.reqparse.parse_args()
        node_1 = args.get('node1')
        node_2 = args.get('node2')

        # Loading Graph
        g = UtilsService.load_graph(UtilsService.FIXTURE_DIRS + "/collisions.data")
        result = g.same_network((node_1, node_2))

        return dict(is_same_network=result), 201
