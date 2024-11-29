from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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





df.to_csv('../data/cleaning_data_step2.csv', index=False)

df = pd.read_csv('../data/cleaning_data_step2.csv')

scaler = MinMaxScaler()
df['area_normalized'] = scaler.fit_transform(df[['area']])

df['area'] = df['area_normalized']
df.drop(columns=['area_normalized'], inplace=True)

df.to_csv('../data/cleaning_data_step3.csv', index=False)

print(df.head())

binary_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'semi_furnished', 'unfurnished']
for col in binary_columns:
    print(f"{col}: {df[col].unique()}")

print(df.isnull().sum())

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.show()

df_cleaned = df.drop(columns=["hotwaterheating", "semi_furnished"])
df_cleaned.to_csv('../data/cleaned_data.csv', index=False)

#todo 
#1 convert variables to binary format 
#2 normalize area 
#3 maybe remove some colums 