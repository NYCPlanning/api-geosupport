from flask import Flask
from flask_restful import Resource, Api, reqparse
from geosupport import Geosupport, GeosupportError

app = Flask(__name__)
api = Api(app)

g = Geosupport()


class GeosupportApi(Resource):
    """
    Supports all functions and arguments of python-geosupport
    """

    def get(self, geofunction):

        params = reqparse.request.args

        try:
            result = g[geofunction](**params)
            return {'error': False, 'result': result}

        except GeosupportError as ge:
            return {'error': True, 'result': ge.result}

        except AttributeError:
            return {'error': True, 'result': {"Message": "Unknown Geosupport function '{}'.".format(geofunction)}}


api.add_resource(GeosupportApi, '/<string:geofunction>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
