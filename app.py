from flask import Flask
from flask_restful import Api

from resources.graph import GraphDetail, GraphList
from resources.node import NodeDetail, NodeCollision

app = Flask(__name__)
api = Api(app)

# Registering Routes
api.add_resource(GraphDetail, '/graph/<int:id>')
api.add_resource(GraphList, '/graph')
api.add_resource(NodeDetail, '/graph/<int:id>/node')
api.add_resource(NodeCollision, '/graph/<int:id>/node/collision')


if __name__ == '__main__':
    app.run(debug=True)