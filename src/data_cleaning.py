
import pandas as pd

df = pd.read_csv('../data/housing_data.csv')


columns_to_convert = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']

for col in columns_to_convert:
    df[col] = df[col].map({'yes': 1, 'no': 0})


print(df.head())
print(df.info())
print(df.tail())
print(df.info())

for col in columns_to_convert:
    print(f"uniquee values {col}: {df[col].unique()}")


df.to_csv('../data/cleaning_data_step1.csv', index=False)


df = pd.read_csv('../data/cleaning_data_step1.csv')

df = pd.get_dummies(df, columns=['furnishingstatus'], drop_first=True)

df.rename(columns={
    'furnishingstatus_semi-furnished': 'semi_furnished',
    'furnishingstatus_unfurnished': 'unfurnished'
}, inplace=True)

boolean_columns = ['semi_furnished', 'unfurnished']
for col in boolean_columns:
    df[col] = df[col].map({True: 1, False: 0})



print(df.head())


df.to_csv('../data/clean_data_step2.csv', index=False)


#todo 
#1 convert variables to binary format 
#2 normalize area 
#3 maybe remove some colums 