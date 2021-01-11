![IMG](demo/banner.png)
Web application: https://car-auction-price.herokuapp.com/

# Car Auction Price Prediction

### Project Overview 

**Goal:**
* Create a tool to predict the auction selling price for cars selling on https://carsandbids.com/
* Practice end-to-end ML development. From data collection to ML model deployment.

**Use Cases:**
* Attract a potential seller by providing an estimate on how much their car could sell for on cars and bids
* Help determine a reserve price
* Help inform a buyer on a how high to bid on a car

I figured using data from cars and bids would be intersting becuase they include the horsepower, torque, and transmission specs of each car. I also know exactly what the car sells for. This is different then kiji autos or auto trader that has a listed price. However, as a smaller, new website there are around 1200 sold cars which is a relatively small training set. Overall, this was an interesting investigation of data quality/features versus quantity of data. 

**Results and Takeaways:** 
* An XG Boost regressor model performed the best with a mean absolute error (MAE) of around $6000
* This means on average the model was $6000 off the correct price of a car. With the average price of a car sold being 
* The model interestinlgy permormed the best on training data by extremely overfitting the data. Looking at the learning curve this means the model would benefit from more training examples.
* Horsepower was the best indictor of selling price
* The model does well on cars where the features accuralty portray the cars worth understanbly
* The model does very poorly on cars that have appreciated in value if it has not specifially been trained on it. A good example is the BMW Z8 which the model predicts to sell around $20 000 but sells for upwards of $180 000 https://carsandbids.com/auctions/92onPXLA/2002-bmw-z8. The BMW Z8 has appreciated greatly in value partly due to it being regarded as a beatiful car but also becuase of its limited production numbers. 
including prodiction numbers could help the model predict these cars but the easiest way would be to train it on more cars including these appreciated cars.
* There 

## Data Collection 

A webscraper was built using selenium and beatiful soup. Files can be found in main.py, scraper.py and the raw data stored in a csv file called car_auction_data. Features collected was vehicle Year,	Make,	Model,	Seller,	Location,	VIN,	Mileage,	BodyStyle,	Engine,	Drivetrain,	Transmission,	ExteriorColor,	InteriorColor,	TitleStatus,	SellerType,	Price,	Reserve,	Horsepower,	Torque.


## Data Cleaning
## Data Exploration 
## Model Training and Hyperparameter tuning
After testing a random forest regressor, Lasso regression, ridge regression, and XG boost resgressor, the  
## Model Explainability
## Model Web Deployment



