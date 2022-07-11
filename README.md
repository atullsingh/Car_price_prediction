# Car_price_prediction using Random Forest
Data is taken from Kaggle and it contains 15407 entries with no NULL values.
Algorithm used is RANDOM Forest
### Hyperparameter tuning is done using Randomized SearchCV
n_estimators = [100,200,300,400,500,600,700,800,900,1000,1100,1200]
max_features = ['auto','sqrt']
max_depth = [5,10,15,20,25,30]
min_samples_split = [2,5,10,15,100]
min_samples_leaf =[1,2,5,10]
Accuracy score is 81.91% 
### Model is deployed using Flask (app1.py)
### Simple HTML template is used (
