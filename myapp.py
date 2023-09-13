from flask import flask, request
from flask_restful import Resource , Api
from flask_cors import CORS
import pickle
import pandas as pd



app = flask(__name__)
CORS(app)
api = Api(app)

class prediction(Resource):
    def get(self,x):
        #x = request.args.get('prediction')
        print(x)
        x = [int(x)]
        df = pd.DataFrame(x, columns=['Good QTY','Scraped QTY'])
        model = pickle.load(open('','rb'))
        prediction = model.predict(df)
        return str(prediction)

'''class getData(Resource):
    def get(self):
         df = pd.read_excel('')
         res = df.to_json(orient='records')
         return res'''
    
api.add_resource(getData , '/api')
api.add_resource(prediction , '/pridiction/<int:x>')

if __name__ == '__main__':
    api.run(debug=True)
