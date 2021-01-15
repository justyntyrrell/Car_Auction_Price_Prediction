![IMG](demo/banner.png)
Web application: https://car-auction-price.herokuapp.com/

# Car Auction Price Prediction

## Project Overview 

**Goal:**
* Create a tool to predict the auction selling price for cars selling on https://carsandbids.com/
* Practice end-to-end machine learning (ML) development. From data collection to model deployment.

![IMG](demo/example1.gif)

**Use Cases:**
* Attract a potential seller by providing an estimate on how much their car could sell for on cars and bids.
* Help determine a reserve price.
* Help inform a buyer on how high to bid on a car.

**Why carsandbids.com?**

I wanted to use cars and bids because they include the horsepower, torque, and transmission specs of each car. It also shows exactly what the car sold for or the highest bid. This is different then Kiji Autos or Auto Trader that has a listed price. However, as a smaller, new website there were around 1200 sold cars at the time of data collection which is a relatively small training set. Overall, this was an interesting investigation of data quality/features versus quantity of data. 

**File Summary:**
* Web Scraper: [main.py](/main.py), [scraper.py](/scraper.py)
* Collected Raw Data: [car_auction_data.csv](/car_auction_data.csv)
* Model building: [car_auction.ipynb](/car_auction.ipynb)
* Flask web app: [app.py](/app.py), [index.html](/templates/index.html), [Procfile](//Procfile), [requirements.txt](/requirements.txt), [OH_encoder.pkl](/OH_encoder.pkl), [Finalized_model.pkl](/Finalized_model.pkl)


**Results and Takeaways:** 
* An XGBoost regressor model performed the best with a mean absolute error (MAE) of around $6900
* This means on average the model was $6900 off the correct price of a car.
* To contextualize this, the average sale price was $20 085 with a std of $21 700
* The model performed the best by overfitting the data. Looking at the learning curve this means the model would benefit from more training examples.
* Horsepower was the best indictor of selling price
* The model understandably does well on cars where the features accurately portray the cars worth
* The model does very poorly on cars that have appreciated in value unless the model has been trained on that particular car. A good example is the BMW Z8 which the model predicts would sell for around $20 000 but actually sells for upwards of $180 000 https://carsandbids.com/auctions/92onPXLA/2002-bmw-z8. The BMW Z8 has appreciated greatly in value partly due to it being regarded as a good looking car but also because of its limited production numbers. 
* Including production numbers could help the model predict these cars but the easiest way would be to train it on more cars including examples of appreciated cars.

## Data Collection 
Libraries used: selenium, beatifulSoup

* A web scraper was built using selenium and beautifulsoup. 
* Features collected were vehicle: Year, Make, Model,	Seller,	Location,	VIN, Mileage, BodyStyle, Engine, Drivetrain, Transmission, ExteriorColor, InteriorColor,	TitleStatus, SellerType, Price,	Reserve, Horsepower, Torque.

## Data Cleaning
Libraries used: pandas, numpy, fuzzywuzzy

* Data was loaded as a panda dataframe in Jupyter notebook. 
* Various characters were removed from numerical data such as commas and $'s. It was then converted to integers. 
* Some categorical data was simplified due to inconsistent data entry. Ex. fuzzywuzzy was used to sort sellertype as "dealer" or "private party" 
* Transmission type was simplified in a similar manner for better categorical encoding 

## Data Exploration 
Libraries used: seaborn, matplotlib
* Various scatter plots, boxplots, and correlation matrix
* Scatter plots showed some larger than possible values (HP > 2000) and these were corrected 
* Horsepower followed by torque has the largest correlation to price

| ![IMG](demo/corrmat.PNG) |
|:--:| 
| *Correlation matrix* |

| ![IMG](demo/scatterplots.png) |
|:--:| 
| *Scatterplot* |

| ![IMG](demo/makeboxplot.png) |
|:--:| 
| *Box plot of car price vs. Make* |

## Model Preprocessing, Training, and Hyperparameter tuning
Libraries used: sklearn, skopt, xgboost

Models tested: Random forest regressor, XGboost regressor, Lasso regression, Ridge regression,
*RFR and XGBoost are descision tree based models. 
*Lasso and Ridge both use regularized linear regression, the difference being how they are regularized. Ridge adds a penalty term which is equal to the square of the coefficient. Lasso adds a penalty term to the cost function. This term is the absolute sum of the coefficients.

* A one hot encoder is used to encode categorical data. (categorical data here is not ordinal. 
* Car makes could be label encoded however. Ex. Ferrari and McLaren labeled as 10, Honda and Ford labeled as 1
* Target encoding tested but OHE provided better results.
* Data split into test and train sets, 10-90
* Model trained, 5-fold cross validation and MAE used to test performance. (CV used due to small dataset is less suceptible to outliers however introduces some data leakage)
* learning curves plotted to check over and underfitting 
* Hyperparameter tuning with gridsearch and Bayesian optimization

## Model Explainability
Libraries used: eli5, shap, graphviz

* Permutation Importance to calculate feature importance. 
* This works by randomly shuffling a feature column in the dataset and making predictions using the resulting dataset. If the model relied on that feature heavily to make accurate predictions then the results will be very off. For example, horsepower is shuffled so a random horsepower stat is assigned to a car. If horsepower is a good predictor of the value of a car, then the prediction using the shuffled dataset will be wildly off.  

| ![IMG](demo/permutationimportance.png) |
|:--:| 
| *Permutation Importance* |

* Feature importance shows what variables most affect predictions, partial dependence plots show how a feature affects predictions.
*  This is done by repeatedly altering the value for one variable and tracing how this impacts the outcome.
* For example, horsepower is increased from 0 to 800 and the predicted price is graphed. This is done for multiple cars and averaged. 

| ![IMG](demo/pdp.png) |
|:--:| 
| *Partial Dependence Plot* |

* SHAP values interpret the impact of having a certain value for a given feature in comparison to the prediction we'd make if that feature took some baseline value.

| ![IMG](demo/SHAP.png) |
|:--:| 
| *SHapley Additive exPlanations* |

* SHAP summary plots show feature importance using permutaion importance but also show what is driving it. 
* Each dot has three characteristics:
  * Vertical location shows what feature it is depicting
  * Color shows whether that feature was high or low for that row of the dataset
  * Horizontal location shows whether the effect of that value caused a higher or lower prediction.

| ![IMG](demo/SHAPsummaryplot.png) |
|:--:| 
| *SHAP Summary Plot* |


## Model Web Deployment
Tech stack: pickle, flask, Heroku

Model trained against entire dataset due to its limited size. The model was then serialized using pickle. 
Web app was made using flask and deployed by linking GitHub with Heroku. 



