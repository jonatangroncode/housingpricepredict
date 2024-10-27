# Housing Price Prediction Project

This document outlines the project plan and initial thoughts for the housing price prediction model. The project aims to utilize **linear regression**, a supervised learning algorithm, to predict the price of a house based on input parameters provided by the user.

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

### Data Preprocessing:
- Convert categorical variables (such as yes/no values) to binary (0/1).
- Clean the data by handling missing values (or changing but i dont think its necessary for now) and normalizing numerical features if necessary. (area)
- Maybe removing columns if necessary 

