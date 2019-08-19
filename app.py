from flask import Flask
from flask_restful import Resource, Api, reqparse
from geosupport import Geosupport, GeosupportError
from suggest import GeosupportSuggest

app = Flask(__name__)
api = Api(app)

g = Geosupport()
s = GeosupportSuggest(g)


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


api.add_resource(GeosupportApi, '/geocode/<string:geofunction>', endpoint='geocode')


class SuggestApi(Resource):
    """
    An address suggestions API
    """

    def get(self):

        try:
            parser = reqparse.RequestParser()
            parser.add_argument('address', type=str, trim=True, required=True)
            parser.add_argument('borough_code', type=int, trim=True, required=False)
            args = parser.parse_args()
            result = s.suggestions(args["address"], borough_code=args["borough_code"])
            return {"error": False, "result": result}
        except Exception as e:
            return {"error": True, "result": str(e)}


api.add_resource(SuggestApi, '/suggest', endpoint='suggest')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
