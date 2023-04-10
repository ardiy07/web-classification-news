import pickle
from app import response, app
from flask import request

def prediction():
    try:
        text = request.form['news']
        clf_filename = './app/model/naive_bayes_classifire.pkl'
        nb_clf = pickle.load(open(clf_filename, 'rb'))
        vec_filename = './app/model/count_vectorize.pkl'
        vec = pickle.load(open(vec_filename,'rb'))
        pred = nb_clf.predict(vec.transform([text]))
        return response.succes(pred[0], 'Succes')
    except Exception:
        return response.badRequest()
