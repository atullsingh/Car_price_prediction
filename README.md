## Heroku app link: https://carprice--predictor.herokuapp.com/


# Car_price_prediction using Random Forest
Data is taken from Kaggle and it contains 15407 entries with no NULL values.
Due size constraint used only 4000 entries
Algorithm used is RANDOM Forest
### Hyperparameter tuning is done using Randomized SearchCV
n_estimators = [100,200,300,400,500,600,700,800,900,1000,1100,1200]
max_features = ['auto','sqrt']
max_depth = [5,10,15,20,25,30]
min_samples_split = [2,5,10,15,100]
min_samples_leaf =[1,2,5,10]
## Accuracy score is 94.17% 
### Model is deployed using Flask (app.py)
### Simple HTML template is used (index.html)
Which takes 'vehicle_age', 'km_driven', 'present_price', 'mileage',
       'seller_type_Dealer', 'seller_type_Individual', 'fuel_type_CNG',
       'fuel_type_Diesel', 'fuel_type_LPG', 'fuel_type_Petrol',
       'transmission_type_Automatic', 'transmission_type_Manual' as a entry
