from flask import jsonify, make_response

# UTIL RESPONSE FOR BOTH SUCCESS AND FAIL CASES


def response(response_type, response_data, status_code):
    return make_response(jsonify({'status': response_type, 'data': response_data}), status_code)
