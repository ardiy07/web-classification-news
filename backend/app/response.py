from flask import jsonify, make_response

def succes( predict, message ):
    res = {
        'predict': predict,
        'message': message
    }

    return make_response(jsonify(res)), 200

def badRequest():
    res = {
        'predict': 'none',
        'message': 'Please re-enter the news that you want to classify, or enter more complex news'
    }

    return make_response(jsonify(res)), 400