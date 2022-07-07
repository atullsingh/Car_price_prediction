from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        vehicle_age = int(request.form['vehicle_age'])
        present_price=float(request.form['present_price'])
        km_driven=int(request.form['km_driven'])
        mileage=float(request.form['mileage'])
        fuel_type_Petrol=request.form['fuel_type_Petrol']
        if(fuel_type_Petrol=='Petrol'):
                fuel_type_Petrol=1
                fuel_type_Diesel=0
                fuel_type_CNG=0
                fuel_type_LPG=0
        elif(fuel_type_Petrol=='Diesel'):
                fuel_type_Petrol=0
                fuel_type_Diesel=1
                fuel_type_CNG=0
                fuel_type_LPG=0
        elif(fuel_type_Petrol=='CNG'):
                fuel_type_Petrol=0
                fuel_type_Diesel=0
                fuel_type_CNG=1
                fuel_type_LPG=0
        if(fuel_type_Petrol=='LPG'):
                fuel_type_Petrol=0
                fuel_type_Diesel=0
                fuel_type_CNG=0
                fuel_type_LPG=1
        seller_type_Individual=request.form['seller_type_Individual']
        if(seller_type_Individual=='Individual'):
            seller_type_Individual=1
            seller_type_Dealer=0
        else:
            seller_type_Individual=0
            seller_type_Dealer=1
        transmission_type_Manual=request.form['transmission_type_Manual']
        if(transmission_type_Manual=='Mannual'):
            transmission_type_Manual=1
            transmission_type_Automatic=0
        else:
            transmission_type_Manual=0
            transmission_type_Automatic=1
        prediction=model.predict([[vehicle_age,km_driven,present_price,mileage,seller_type_Dealer,seller_type_Individual,fuel_type_CNG,fuel_type_Diesel,fuel_type_LPG,fuel_type_Petrol,transmission_type_Automatic,transmission_type_Manual]])
        output=round(prediction[0])
        if output<0:
            return render_template('index.html',prediction_text="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

