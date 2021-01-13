![IMG](demo/banner.png)
Web application: https://car-auction-price.herokuapp.com/

# Car Auction Price Prediction

### Project Overview 

**Goal:**
* Create a tool to predict the auction selling price for cars selling on https://carsandbids.com/
* Practice end-to-end ML development. From data collection to ML model deployment.

![IMG](demo/example1.gif)

**Use Cases:**
* Attract a potential seller by providing an estimate on how much their car could sell for on cars and bids
* Help determine a reserve price
* Help inform a buyer on how high to bid on a car

I wanted to use cars and bids in particular becuase they include the horsepower, torque, and transmission specs of each car. It also shows exactly what the car sold for or the highest bid. This is different then kiji auto or auto trader that has a listed price. However, as a smaller, new website there were around 1200 sold cars at the time of data collection which is a relatively small training set. Overall, this was an interesting investigation of data quality/features versus quantity of data. 

**Results and Takeaways:** 
* An XG Boost regressor model performed the best with a mean absolute error (MAE) of around $6900
* This means on average the model was $6900 off the correct price of a car.
* To contextualize this, the average sale price was $20 085 with a std of $21 700
* The model actually performed the best by overfitting the data. Looking at the learning curve this means the model would benefit from more training examples.
* Horsepower was the best indictor of selling price
* The model understandbly does well on cars where the features accuralty portray the cars worth
* The model does very poorly on cars that have appreciated in value, unless the model has been trained on that particular car. A good example is the BMW Z8 which the model predicts would sell for around $20 000 but actually sells for upwards of $180 000 https://carsandbids.com/auctions/92onPXLA/2002-bmw-z8. The BMW Z8 has appreciated greatly in value partly due to it being regarded as a beatiful car but also becuase of its limited production numbers. 
* Including prodiction numbers could help the model predict these cars but the easiest way would be to train it on more cars including examples of appreciated cars.

## Data Collection 
Libraries used: selenium, beatifulSoup

* A webscraper was built using selenium and beatiful soup. 
* Files can be found in main.py, scraper.py and the raw data stored in a csv file  car_auction_data. 
* Features collected were vehicle: Year,	Make,	Model,	Seller,	Location,	VIN,	Mileage,	BodyStyle,	Engine,	Drivetrain,	Transmission,	ExteriorColor,	InteriorColor,	TitleStatus,	SellerType,	Price,	Reserve,	Horsepower,	Torque.

## Data Cleaning
Libraries used: pandas, numpy, fuzzywuzzy

* Data was loaded as a panda dataframe in jupyter notenook. 
* Various characters were removed from numerical data such as commas and $'s. It was then converted to integers. 
* Some categorical data was simplified due to different inconsistent data entry. Ex. fuzzywuzzy was used to sort data into sellertype "dealer" or "private party" 
* Transmission type was simplified in a similar manner for better catagorical endcoding 

## Data Exploration 
Libraries used: seaborn, matplotlib
* Various scatter plots, boxplots, and correlation matrix
* scatter plots showed some larger then possible values (HP > 2000) and these were corrected 
*
![IMG](corrmat.png)
![IMG](scatterplot.png)

## Model Training and Hyperparameter tuning
Models tested: Random forest regressor, Lasso regression, ridge regression, and XG boost resgressor
Hyperparameter tuning with bayesion optimization
Data split into test and train sets. 
One hot encoding used on categorical data. Target encoding tested but OHE provided better results.
Cross validation and MAE was used to check performance. A learning curve plotting training size Vs MAE to check over and under fitting.

## Model Explainability


## Model Web Deployment
Model trained agaisnt enitire dataset due to its ilmited size. The model was then serialized using pickle. 
Web app was made using flask.  


