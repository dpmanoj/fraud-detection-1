from flask_restful import Resource, reqparse


class NodeDetail(Resource):
    def get(self, id):
        return {'hello': 'Details'}

    def post(self):
        pass


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

    def post(self, id):
        args = self.reqparse.parse_args()
        print args
        return "Ok", 201


class NodeList(Resource):
    def get(self):
        return {'hello': 'world'}