from flask import Flask
from flask_restful import Api

from private import config
from resources.node import NodeDetail, NodeCollision

app = Flask(__name__)
api = Api(app)

FIXTURE_DIR = config.FIXTURE_DIRS


# Registering Routes
api.add_resource(NodeCollision, '/graph/collision')
api.add_resource(NodeDetail, '/graph/node/collision')


if __name__ == '__main__':
    app.run(debug=True)