# -*- coding: utf-8 -*-
"""OmidBeZendegi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10W80uCxite1r89eTkYGYUXMIxjm7Zz3h
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.compose import make_column_selector as selector
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error, recall_score, precision_score
from sklearn.metrics import mean_squared_error

# Data Loading and Separation: Reads an Excel file into a pandas DataFrame (data)
data = pd.read_excel('OmideBzendegi.xlsx')

# Separate input features and target variable
X = data.iloc[:, 0:]  # Assuming the input features start from the second column
y = data.iloc[:, 0]  # Assuming the output is in the first column


# Data Preprocessing Setup: Converts the 'lastPost-date' column to a datetime format.
# Identifies different types of features: numeric, datetime, and non-numeric (object) features.
X['lastPost-date'] = pd.to_datetime(X['lastPost-date'], errors='coerce')
numeric_features = X.select_dtypes(include=['float64', 'int64']).columns
date_features = X.select_dtypes(include=['datetime']).columns
non_numeric_features = X.select_dtypes(include=['object']).columns


# Preprocessing Pipeline Setup: Defines separate pipelines for numeric and non-numeric (categorical) features.
# Utilizes SimpleImputer for missing values and StandardScaler for numeric features, while using SimpleImputer and
# OneHotEncoder for non-numeric features. These are combined using ColumnTransformer.

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

non_numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse=False))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, numeric_features),
    ('non_num', non_numeric_transformer, non_numeric_features)
])

# Model Creation: Constructs a pipeline for the overall process.
# It includes the preprocessing steps defined earlier and a logistic regression classifier as the final step.


model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])


# Training and Evaluation: Splits the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#fits the model to the training data
model.fit(X_train, y_train)

# makes predictions on the test set
y_pred = model.predict(X_test)

#calculates the accuracy
accuracy = accuracy_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"LogisticRegression Model Accuracy: {accuracy * 100:.2f}%","\n")

print("Mean squared error of the LogisticRegression model: {:.2f}%".format(mse),"\n")

mae = mean_absolute_error(y_test, y_pred)
print("Mean absolute error of the LogisticRegression model: {:.2f}%".format(mae), "\n")

recall = recall_score(y_test, y_pred, average='weighted') * 100
print("Recall of the LogisticRegression model: {:.2f}%".format(recall), "\n")

precision = precision_score(y_test, y_pred, average='weighted') * 100
print("Precision of the LogisticRegression model: {:.2f}%".format(precision), "\n")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error
from sklearn.compose import make_column_selector as selector
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error, recall_score, precision_score

# Data Loading and Separation: Reads an Excel file into a pandas DataFrame (data)
data = pd.read_excel('OmideBzendegi.xlsx')

# Separate input features and target variable
X = data.iloc[:,0:]  # Assuming the input features start from the second column
y = data.iloc[:, 0]  # Assuming the output is in the first column


# Data Preprocessing Setup: Converts the 'lastPost-date' column to a datetime format.
# Identifies different types of features: numeric, datetime, and non-numeric (object) features.
X['lastPost-date'] = pd.to_datetime(X['lastPost-date'], errors='coerce')
numeric_features = X.select_dtypes(include=['float64', 'int64']).columns
date_features = X.select_dtypes(include=['datetime']).columns
non_numeric_features = X.select_dtypes(include=['object']).columns


# Preprocessing Pipeline Setup: Defines separate pipelines for numeric and non-numeric (categorical) features.
# Utilizes SimpleImputer for missing values and StandardScaler for numeric features, while using SimpleImputer and
# OneHotEncoder for non-numeric features. These are combined using ColumnTransformer.

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

non_numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse=False))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, numeric_features),
    ('non_num', non_numeric_transformer, non_numeric_features)
])

# Model Creation: Constructs a pipeline for the overall process.
# It includes the preprocessing steps defined earlier and a NB classifier as the final step.


model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', GaussianNB())
])


# Training and Evaluation: Splits the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#fits the model to the training data
model.fit(X_train, y_train)

# makes predictions on the test set
y_pred = model.predict(X_test)

#calculates the accuracy
accuracy = accuracy_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"Naive Bayes Model Accuracy: {accuracy * 100:.2f}%","\n")

print("Mean squared error of the Naive Bayes model: {:.2f}%".format(mse),"\n")

mae = mean_absolute_error(y_test, y_pred)
print("Mean absolute error of the Naive Bayes model: {:.2f}%".format(mae), "\n")

recall = recall_score(y_test, y_pred, average='weighted') * 100
print("Recall of the Naive Bayes model: {:.2f}%".format(recall), "\n")

precision = precision_score(y_test, y_pred, average='weighted') * 100
print("Precision of the Naive Bayes model: {:.2f}%".format(precision), "\n")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, recall_score, precision_score
from sklearn.svm import SVR

# Data Loading and Separation
data = pd.read_excel('OmideBzendegi.xlsx')
X = data.iloc[:, 0:]  # Assuming the input features start from the second column
y = data.iloc[:, 0]   # Assuming the output is in the first column

# Data Preprocessing Setup
X['lastPost-date'] = pd.to_datetime(X['lastPost-date'], errors='coerce')
numeric_features = X.select_dtypes(include=['float64', 'int64']).columns
non_numeric_features = X.select_dtypes(include=['object']).columns

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

non_numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse=False))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, numeric_features),
    ('non_num', non_numeric_transformer, non_numeric_features)
])

# Model Creation
model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', SVR())
])

# Training and Evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Calculate and display metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
recall = recall_score(y_test, y_pred.round(), average='macro')  # Use 'macro' for multiple classes
precision = precision_score(y_test, y_pred.round(), average='macro')  # Use 'macro' for multiple classes
accuracy = 1 - mse / y_test.var()

print(f"SVR Model Accuracy: {accuracy * 100:.2f}%","\n")
print("Mean squared error of the SVR model: {:.2f}%".format(mse), "\n")
print("Mean absolute error of the SVR model: {:.2f}%".format(mae), "\n")
print("Recall of the SVR model: {:.2f}%".format(recall*100 ), "\n")
print("Precision of the SVR model: {:.2f}%".format(precision*100), "\n")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, precision_score, recall_score

# Data Loading and Separation: Reads an Excel file into a pandas DataFrame (data)
data = pd.read_excel('OmideBzendegi.xlsx')

# Separate input features and target variable
X = data.iloc[:, 0:]  # Assuming the input features start from the second column
y = data.iloc[:, 0]  # Assuming the output is in the first column

# Data Preprocessing Setup: Converts the 'lastPost-date' column to a datetime format.
# Identifies different types of features: numeric, datetime, and non-numeric (object) features.
X['lastPost-date'] = pd.to_datetime(X['lastPost-date'], errors='coerce')
numeric_features = X.select_dtypes(include=['float64', 'int64']).columns
date_features = X.select_dtypes(include=['datetime']).columns
non_numeric_features = X.select_dtypes(include=['object']).columns

# Preprocessing Pipeline Setup: Defines separate pipelines for numeric and non-numeric (categorical) features.
# Utilizes SimpleImputer for missing values and StandardScaler for numeric features, while using SimpleImputer and
# OneHotEncoder for non-numeric features. These are combined using ColumnTransformer.

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

non_numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse=False))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, numeric_features),
    ('non_num', non_numeric_transformer, non_numeric_features)
])

# Model Creation: Constructs a pipeline for the overall process.
# It includes the preprocessing steps defined earlier and a linear regression classifier as the final step.

model = Pipeline([
    ('preprocessor', preprocessor),
    ('poly', PolynomialFeatures(degree=2)),
    ('classifier', LinearRegression())
])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the testing set
predictions = model.predict(X_test)

# Calculate and display the metrics
mse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
recall = recall_score(y_test, predictions.round(), average='weighted')
precision = precision_score(y_test, predictions.round(), average='weighted')
accuracy = 1 - mse / y_test.var()

print("Accuracy of the Polynomial model: {:.2f}%".format(accuracy * 100), "\n")
print("Mean squared error of the Polynomial model: {:.2f}%".format(mse), "\n")
print("Mean absolute error of the Polynomial model: {:.2f}%".format(mae), "\n")
print("Recall of the Polynomial model: {:.2f}%".format(recall * 100), "\n")
print("Precision of the Polynomial model: {:.2f}%".format(precision * 100), "\n")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error, recall_score, precision_score
from sklearn.tree import DecisionTreeClassifier

# Data Loading and Separation: Reads an Excel file into a pandas DataFrame (data)
data = pd.read_excel('OmideBzendegi.xlsx')

# Separate input features and target variable
X = data.iloc[:, 1:]  # Assuming the input features start from the second column
y = data.iloc[:, 0]  # Assuming the output is in the first column

# Data Preprocessing Setup: Converts the 'lastPost-date' column to a datetime format.
# Identifies different types of features: numeric, datetime, and non-numeric (object) features.
X['lastPost-date'] = pd.to_datetime(X['lastPost-date'], errors='coerce')
numeric_features = X.select_dtypes(include=['float64', 'int64']).columns
date_features = X.select_dtypes(include=['datetime']).columns
non_numeric_features = X.select_dtypes(include=['object']).columns

# Preprocessing Pipeline Setup: Defines separate pipelines for numeric and non-numeric (categorical) features.
# Utilizes SimpleImputer for missing values and StandardScaler for numeric features, while using SimpleImputer and
# OneHotEncoder for non-numeric features. These are combined using ColumnTransformer.

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

non_numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse=False))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, numeric_features),
    ('non_num', non_numeric_transformer, non_numeric_features)
])

# Model Creation: Constructs a pipeline for the overall process.
# It includes the preprocessing steps defined earlier and a Decision Tree classifier as the final step.

model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', DecisionTreeClassifier())
])

# Training and Evaluation: Splits the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fits the model to the training data
model.fit(X_train, y_train)

# Makes predictions on the test set
y_pred = model.predict(X_test)

# Calculates and displays the metrics
accuracy = accuracy_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"Decision Tree Model Accuracy: {accuracy * 100:.2f}%","\n")

print("Mean squared error of the Decision Tree model: {:.2f}%".format(mse),"\n")

mae = mean_absolute_error(y_test, y_pred)
print("Mean absolute error of the Decision Tree model: {:.2f}%".format(mae), "\n")

recall = recall_score(y_test, y_pred, average='weighted') * 100
print("Recall of the Decision Tree model: {:.2f}%".format(recall), "\n")

precision = precision_score(y_test, y_pred, average='weighted') * 100
print("Precision of the Decision Tree model: {:.2f}%".format(precision), "\n")

import matplotlib.pyplot as plt

# Performance criteria and their corresponding values
performance_criteria = ['accuracy_score', 'precision', 'recall', 'mae', 'mean_squared_error']
values = [64.29, 46.03, 64.29, 2.50, 19.64]

# Create a bar graph
plt.bar(performance_criteria, values, color ='green')

# Add labels and title
plt.xlabel('Performance Criteria')
plt.ylabel('Percentage')
plt.title('Performance Evaluation of Logistic Regression')

# Display the graph
plt.show()

import matplotlib.pyplot as plt

# Performance criteria and their corresponding values
performance_criteria = ['accuracy_score', 'precision', 'recall', 'mae', 'mean_squared_error']
values = [71.43, 71.43, 71.43, 1.79, 12.50]

# Create a bar graph
plt.bar(performance_criteria, values, color ='green')

# Add labels and title
plt.xlabel('Performance Criteria')
plt.ylabel('Percentage')
plt.title('Performance Evaluation of Naive Bayes')

# Display the graph
plt.show()

import matplotlib.pyplot as plt

# Performance criteria and their corresponding values
performance_criteria = ['accuracy_score', 'precision', 'recall', 'mae', 'mean_squared_error']
values = [31.93, 10.00, 7.14, 3.84, 33.01]

# Create a bar graph
plt.bar(performance_criteria, values, color ='green')

# Add labels and title
plt.xlabel('Performance Criteria')
plt.ylabel('Percentage')
plt.title('Performance Evaluation of SVR')

# Display the graph
plt.show()

import matplotlib.pyplot as plt

# Performance criteria and their corresponding values
performance_criteria = ['accuracy_score', 'precision', 'recall', 'mae', 'mean_squared_error']
values = [67.16, 64.29, 50.00, 1.78, 15.93]

# Create a bar graph
plt.bar(performance_criteria, values, color ='green')

# Add labels and title
plt.xlabel('Performance Criteria')
plt.ylabel('Percentage')
plt.title('Performance Evaluation of Polynomial Regression')

# Display the graph
plt.show()

import matplotlib.pyplot as plt

# Performance criteria and their corresponding values
performance_criteria = ['accuracy_score', 'precision', 'recall', 'mae', 'mean_squared_error']
values = [28.57, 28.57, 28.57, 5.71, 57.14]

# Create a bar graph
plt.bar(performance_criteria, values, color ='green')

# Add labels and title
plt.xlabel('Performance Criteria')
plt.ylabel('Percentage')
plt.title('Performance Evaluation of Decision Tree')

# Display the graph
plt.show()