from flask import Flask, jsonify, request, render_template
from geosupport import Geosupport, GeosupportError
import os 

g = Geosupport()
app = Flask(__name__)

BOROUGHS = {
    'MANHATTAN': 1, 'MN': 1, 'NEW YORK': 1, 'NY': 1,
    'BRONX': 2, 'THE BRONX': 2, 'BX': 2,
    'BROOKLYN': 3, 'BK': 3, 'BKLYN': 3, 'KINGS': 3,
    'QUEENS': 4, 'QN': 4, 'QU': 4,
    'STATEN ISLAND': 5, 'SI': 5, 'STATEN IS': 5, 'RICHMOND': 5,
    '': '',
}

@app.route('/<function>/', methods=['GET'])
def geocode(function):
    house_number = request.args.get('house_number', '')
    street_name = request.args.get('street_name', '')
    borough = request.args.get('borough', '')
    zip_code = request.args.get('zipcode', '')
    mode = request.args.get('mode', 'regular')

    return get_1A_1B_1E(function=function,
                        house_number=house_number,
                        street_name=street_name, 
                        borough=borough,
                        zip_code=zip_code, 
                        mode=mode, 
                        subset=False)

@app.route('/BN/', methods=['GET'])
def BN():
    bin = request.args.get('bin')
    mode = request.args.get('mode', 'regular')
    try:
        geo = g['BN'](bin=bin, mode=mode)
        return jsonify({'status':'success', 
                            'inputs': {
                                'function': 'BN',
                                'bin': bin,
                                'mode': mode
                            },
                            'results': geo
                            })
    except GeosupportError as e:
        return jsonify({'status':'failure', 
                            'inputs': {
                                'function': 'BN',
                                'bin': bin,
                                'mode': mode
                            },
                            'results': e.result
                            })

@app.route('/BL/', methods=['GET'])
def BL():
    bbl = request.args.get('bbl')
    mode = request.args.get('mode', 'regular')
    try:
        geo = g['BL'](bbl=bbl, mode=mode)
        return jsonify({'status':'success', 
                            'inputs': {
                                'function': 'BL',
                                'bbl': bbl,
                                'mode': mode
                            },
                            'results': geo
                            })
    except GeosupportError as e:
        return jsonify({'status':'failure', 
                            'inputs': {
                                'function': 'BL',
                                'bbl': bbl,
                                'mode': mode
                            },
                            'results': e.result
                            })

@app.route('/subset/<function>/', methods=['GET'])
def geocode_subset(function):
    house_number = request.args.get('house_number', '')
    street_name = request.args.get('street_name', '')
    borough = request.args.get('borough', '')
    zip_code = request.args.get('zipcode', '')
    mode = request.args.get('mode', 'regular')

    return get_1A_1B_1E(function=function, 
                        house_number=house_number, 
                        street_name=street_name, 
                        borough=borough,
                        zip_code=zip_code, 
                        mode=mode, 
                        subset=True)
            
def get_1A_1B_1E(function, house_number, street_name, borough, zip_code, mode, subset):
    if mode not in ['regular', 'extended', 'long', 'long+tpad', 'tpad']: 
        return jsonify({
            'status' : 'failure',
            'reason' :  f'mode: {mode} is not recognized'
        })
    else: 
        try: 
            geo = g[function](house_number=house_number, 
                            street_name=street_name, 
                            borough=borough,
                            zip_code=zip_code,
                            mode=mode)

            return jsonify({'status':'success', 
                            'inputs': {
                                'function': function,
                                'house_number': house_number, 
                                'street_name': street_name, 
                                'borough': borough,
                                'zipcode': zip_code, 
                                'mode': mode
                            },
                            'results': get_subset(geo) if subset else geo
                            })

        except GeosupportError as e: 

            return jsonify({'status': 'failure',
                            'inputs': {
                                'function': function,
                                'house_number': house_number,
                                'street_name': street_name,
                                'borough': borough,
                                'zipcode': zip_code,
                                'mode': mode
                            }, 
                            'results': get_subset(e.result) if subset else e.result
                            })

def get_subset(geo):
    borocode = geo.get('BOROUGH BLOCK LOT (BBL)', {}).get('Borough Code', '')
    firstboro = geo.get('First Borough Name', '')
    return {
            'First Street Name Normalized' : geo.get('First Street Name Normalized', ''),
            'House Number - Display Format' : geo.get('House Number - Display Format', ''),
            'First Borough Name' : geo.get('First Borough Name', ''),
            'Latitude' : geo.get('Latitude', ''),
            'Longitude' : geo.get('Longitude', ''),

            'Building Identification Number (BIN) of Input Address or NAP' : geo.get('Building Identification Number (BIN) of Input Address or NAP',''),
            'BOROUGH BLOCK LOT (BBL)' : geo.get('BOROUGH BLOCK LOT (BBL)', {}).get('BOROUGH BLOCK LOT (BBL)', ''),
            'Borough Code' : borocode if borocode != '' else str(BOROUGHS.get(firstboro, '')),

            'Community School District' : geo.get('Community School District', ''),
            'COMMUNITY DISTRICT' : geo.get('COMMUNITY DISTRICT', {}).get('COMMUNITY DISTRICT', ''),
            '2010 Census Tract' : geo.get('2010 Census Tract', ''),
            'City Council District' : geo.get('City Council District', ''),
            'ZIP Code' : geo.get('ZIP Code', ''),
            'USPS Preferred City Name' : geo.get('USPS Preferred City Name', ''), 
            'Spatial X-Y Coordinates of Address' : geo.get('Spatial X-Y Coordinates of Address', ''), 
            'Neighborhood Tabulation Area (NTA)' : geo.get('Neighborhood Tabulation Area (NTA)', ''), 
            'City Council District' : geo.get('City Council District', ''), 
            'Police Precinct' : geo.get('Police Precinct', ''), 

            'Geosupport Return Code (GRC)' : geo.get('Geosupport Return Code (GRC)', ''),
            'Geosupport Return Code 2 (GRC 2)' : geo.get('Geosupport Return Code 2 (GRC 2)', ''),
            'Message' : geo.get('Message', 'msg err'),
            'Message 2' : geo.get('Message 2', 'msg2 err'),
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)