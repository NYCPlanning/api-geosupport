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
        except GeosupportError as ge:
            return {
                'error': True,
                'result': ge.result
            }

        return {
            'error': False,
            'result': result
        }


api.add_resource(GeosupportApi, '/geosupport/<string:geofunction>')

if __name__ == '__main__':
    app.run(debug=True)
