import json

# UTIL RESPONSE FOR BOTH SUCCESS AND FAIL CASES


def response(response_type, response_data, status_code):
    return json.dumps({'status': response_type, 'data': response_data}), status_code, {'ContentType': 'application/json'}
