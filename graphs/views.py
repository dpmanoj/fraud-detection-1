import json
import logging

from django.http import JsonResponse
from rest_framework.views import APIView

from .utils import UtilsService, DuplicateEdgeError, NodeDoesntExistError

logger = logging.getLogger(__name__)


class NodeDetail(APIView):
    """
    Insert new collisions in the graph, remember that two collisions are represented 
    by a pair (x, y) that is a edge in graph structure
    """

    def post(self, request, format=None):

        # Setting default responses
        try:
            status = 201

            data = json.loads(request.body)

            # Get args
            node_1 = data.get('node1')
            node_2 = data.get('node2')

            if node_1 is not None and node_2 is not None:
                node_1 = int(node_1) if isinstance(node_1, str) and node_1.isdigit() else node_1
                node_2 = int(node_2) if isinstance(node_2, str) and node_2.isdigit() else node_2

                # Loading Graph
                g = UtilsService.load_graph()

                # Insert new node, we can adding new nodes directly say what edge, i
                # f some of node doesn't exist we'll create
                g.add_node(nodes=[node_1, node_2])
                g.add_edge(edge=(node_1, node_2))

                UtilsService.store_graph((node_1, node_2))

                d = dict(message="Resource created with successful",
                         edge=(node_1, node_2),
                         status=201)
            else:
                status = 400
                d = dict(message="Bad Request",
                         status=status)

        except DuplicateEdgeError:
            status = 409
            d = dict(message="Resource already exist",
                     status=409)

        return JsonResponse(data=d,
                            status=status)


class NodeCollision(APIView):
    """
    Check when two nodes was in the same network collision
    """

    def post(self, request, format=None):

        """
        I chosen make a operation that not represent directly a resource using the POST verb, 
        but this is a open question when we work with restful, I chosen this way because I think that is
        a acceptable way to do and not is a anti-pattern.

        :param kwargs: 
        :return: json with result of operation
        """

        try:
            data = json.loads(request.body)

            # Get args
            node_1 = data.get('node1')
            node_2 = data.get('node2')

            if node_1 is not None and node_2 is not None:
                node_1 = int(node_1) if isinstance(node_1, str) and node_1.isdigit() else node_1
                node_2 = int(node_2) if isinstance(node_2, str) and node_2.isdigit() else node_2

                # Loading Graph
                g = UtilsService.load_graph()
                result = g.same_network((node_1, node_2))

                d = dict(is_same_network=result)
                status = 201

            else:
                status = 400
                d = dict(message="Bad Request",
                         status=status)

        except NodeDoesntExistError:
            status = 403

            d = dict(message="Resource not found",
                     status=403)

        return JsonResponse(data=d,
                            status=status)
