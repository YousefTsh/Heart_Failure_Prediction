from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import numpy as np
import pickle as p
import json

app = Flask(__name__)
api = Api(app)


predict_put_args = reqparse.RequestParser()

predict_put_args.add_argument("age", type=int, help="Age is required", required=True)
predict_put_args.add_argument("anaemia", type=int, help="anemia is required", required=True)
predict_put_args.add_argument("creatinine_phosphokinase", type=int, help="creatinine_phosphokinase is required", required=True)
predict_put_args.add_argument("diabetes", type=int, help="diabetes is required", required=True)
predict_put_args.add_argument("ejection_fraction", type=int, help="ejection_fraction is required", required=True)
predict_put_args.add_argument("high_blood_pressure", type=int, help="high_blood_pressure is required", required=True)
predict_put_args.add_argument("platelets", type=float, help="platelets is required", required=True)
predict_put_args.add_argument("serum_creatinine", type=float, help="serum_creatinine is required", required=True)
predict_put_args.add_argument("sex", type=int, help="sex is required", required=True)
predict_put_args.add_argument("smoking", type=int, help="smoking is required", required=True)
predict_put_args.add_argument("time", type=int, help="time is required", required=True)
predict_put_args.add_argument("serum_sodium", type=int, help="serum_sodium is required", required=True)

predict = {}

class Prediction(Resource):
    def put(self, prediction_id):
        args = predict_put_args.parse_args()
        predict[prediction_id] = args
        return predict[prediction_id], 201 #created
    
    def get(self, prediction_id):
        data_list = []
        data_list.append(predict[prediction_id]["age"])
        data_list.append(predict[prediction_id]["anaemia"])
        data_list.append(predict[prediction_id]["creatinine_phosphokinase"])
        data_list.append(predict[prediction_id]["diabetes"])
        data_list.append(predict[prediction_id]["ejection_fraction"])
        data_list.append(predict[prediction_id]["high_blood_pressure"])
        data_list.append(predict[prediction_id]["platelets"])
        data_list.append(predict[prediction_id]["serum_creatinine"])
        data_list.append(predict[prediction_id]["serum_sodium"])
        data_list.append(predict[prediction_id]["sex"])
        data_list.append(predict[prediction_id]["smoking"])
        data_list.append(predict[prediction_id]["time"])

        d_test = np.asarray(data_list)
        D = np.reshape(d_test, (1, 12))
        prediction = model.predict(D)
        j_prediction = np.array2string(prediction)
        
        if float(j_prediction[1:-1]) > 1:
            j_prediction = '[1]'
        elif float(j_prediction[1:-1]) < 0:
            j_prediction = '[0]'
        print(j_prediction)
            
        return jsonify(j_prediction)

@app.route('/p', methods=['POST'])
def post():
    args = request.data
    predict = args
    converted = json.loads(args.decode('utf-8'))
    print(converted)
    data_list = []
    data_list.append(converted['age'])
    data_list.append(converted["anaemia"])
    data_list.append(converted["creatinine_phosphokinase"])
    data_list.append(converted["diabetes"])
    data_list.append(converted["ejection_fraction"])
    data_list.append(converted["high_blood_pressure"])
    data_list.append(converted["platelets"])
    data_list.append(converted["serum_creatinine"])
    data_list.append(converted["serum_sodium"])
    data_list.append(converted["sex"])
    data_list.append(converted["smoking"])
    data_list.append(converted["time"])
    d_test = np.asarray(data_list)
    D = np.reshape(d_test, (1, 12))
    prediction = model.predict(D)
    j_prediction = np.array2string(prediction)
    return {'name':j_prediction}




    


api.add_resource(Prediction, "/pred/<int:prediction_id>")

if __name__ == "__main__":
    modelfile = '76%accuracy.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True)