from flask import Flask, jsonify, request 
from geosupport import Geosupport, GeosupportError

g = Geosupport()
app = Flask(__name__)

@app.route('/<function>/', methods=['GET'])
def geocode(function):
    house_number = request.args.get('house_number', '')
    street_name = request.args.get('street_name', '')
    borough = request.args.get('borough', '')
    zipcode = request.args.get('zipcode', '')
    try: 
        geo = g[function](house_number=house_number, 
                        street_name=street_name, 
                        borough=borough,
                        zip_code=zipcode)

        return jsonify({'status':'success', 
                        'inputs': {
                            'function': function,
                            'house_number': house_number, 
                            'street_name': street_name, 
                            'borough': borough,
                            'zipcode': zipcode
                        },
                        'results': geo})

    except GeosupportError as e: 

        return jsonify({'status': 'failure',
                        'inputs': {
                            'function': function,
                            'house_number': house_number, 
                            'street_name': street_name, 
                            'borough': borough, 
                            'zipcode': zipcode
                        }, 
                        'results': {
                            'GRC': e.result['Geosupport Return Code (GRC)'], 
                            'GRC2': e.result['Geosupport Return Code 2 (GRC 2)'],
                            'message1': e.result['Message'],
                            'message2': e.result['Message 2']
                            }
                        })

if __name__ == '__main__':
    app.run(debug=False)
