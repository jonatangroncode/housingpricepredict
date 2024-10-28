# Housing Price Prediction Project

This document outlines the project plan and initial thoughts for the housing price prediction model. The project aims to utilize **multiple linear regression**, a supervised learning algorithm, to predict the price of a house based on input parameters provided by the user.

## Specification

### Application Description:
The application will use a CSV file containing **546 rows** of house data (before data cleaning). This data will be used to train the machine learning model to predict house prices. After training, the user will be able to input specific features about a house, and the model will return a predicted price.

### Features (Input Parameters):
The user will input the following features, which will be used by the model to make predictions:

- **area** (in square meters)
- **bedrooms**
- **bathrooms**
- **stories**
- **parking spaces**

### Additional Features (To be processed):
Some additional features may be included once data cleaning and transformation (e.g., converting categorical variables to binary) is complete:

- **mainroad** (yes/no)
- **guestroom** (yes/no)
- **basement** (yes/no)
- **hotwaterheating** (yes/no)
- **airconditioning** (yes/no)
- **prefarea** (yes/no)
- **furnishingstatus** (furnished, semi-furnished, unfurnished)

### Algorithms 
- **multiple linear regression**
- **Ridge regression or Lasso regression** (if the dataset is Multicollinearity)
(If the data set is Multicollinearity it can lead to high variance in the coefficients)
- **Alternatively RandomForest regression** (if the complexity is to high and the data have none liniar ralations )

## Data
I will be using a csv file from Keggler (The dataset has 13 features and 546 samples.)
[Kaggle](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)

### Data Preprocessing:
- Convert categorical variables (such as yes/no values) to binary (0/1).
- Clean the data by handling missing values (or changing but i dont think its necessary for now) and normalizing numerical features if necessary. ex(area)
- Maybe removing columns if necessary (feautures that not going to brig mutch to the model, ex only one value or equaly spread out value)

## Librariess

-**pandas:** Data manipulation and analysis
-**scikit-learn:** machine learning algorithms and preprocessing
-**numpy:** numerical operations
-**matplotlib:** vizualisation (maybe some piecharts and histograms to get better understanding of data)
-**flask:** comminucation between backend logic and user interface with server (maybe if im using webaplication instead of prompt) 
-**streamlit:** tool to transform python scripts into interactiv web apps( maybe if im uusing webaplication instead of prompt)  

## Classes and methods
**Housing Data**
-load_data()
-clean_data()
-feature_selection ()
-normalize_features()

**TrainModel**
-train_model()
-load_model()
-store_model()

**Application**
-get_user_data()
-run_application()

**PredictPrice**
-predict_price(userinput)



## Discussions
Initially, I aimed to train, validate, and evaluate the model using data from Swedish housing. I started by exploring the pyscbwrapper library from Statistics Sweden (SCB) to access their API, but I couldn't find the specific data I needed. Additionally, I preferred not to incur costs for accessing particular datasets.

Next, I investigated Hemnet and Booli to see if they provided relevant data. However, Hemnet doesn’t make such data available publicly, and while Booli used to have an API, it is no longer accessible. I also considered web scraping data from Hemnet or Booli, but this approach seemed legally questionable without explicit permission. Since both sites lack APIs, I chose not to pursue scraping further.

After an extensive search, I found a dataset on GitHub containing prices for Stockholm apartments, but it was scraped from Booli, so I decided not to use it for ethical reasons.

Ultimately, I selected a CSV file from Kaggle containing 546 rows of housing data for this project, i think its a good first data set for learning supervised learning. It dosent have missing values and the format looks good but i have to do some cleaning, normalization and changing some colums to binary format instead. 

As machine learning and python is a new feald for me, I decided not to go for reinforcements learning and unsupertized learning as my first project. I think i found a good starter data set for learning. And supervised learning seamed like the best option to start with with the time limitations in mind. And if it goes to well i can always add more or focus on learning and understanding. 