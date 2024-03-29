# -*- coding: utf-8 -*-
"""Kamalgera.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iwteFs8ka7IuWYAgpFQVs68H9Iko6tMV
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the dataset
file_path = "Kamalgera.xlsx"
df = pd.read_excel(file_path)

# Extract the features (from the third column to the last)
features = df.iloc[:, 0:]

# Step 1: Handle missing values (if any)
# For example, you can replace missing values with the mean of each column
features = features.fillna(features.mean())

# Step 2: Encode categorical variables (if any)
# Use LabelEncoder to convert categorical variables into numeric values
label_encoder = LabelEncoder()

for column in features.select_dtypes(include=['object']).columns:
    features[column] = label_encoder.fit_transform(features[column])

# Step 3: Normalize numerical features
#using StandardScaler to standardize the numerical features
scaler = StandardScaler()
normalized_features = pd.DataFrame(scaler.fit_transform(features), columns=features.columns)

# Show the new dataset
print(normalized_features)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, mean_squared_error,mean_absolute_error, recall_score, precision_score

# Load the dataset
file_path = "Kamalgera.xlsx"
df = pd.read_excel(file_path)

# Extract the features (from the third column to the last)
features = df.iloc[:, 0:]

# Step 1: Handle missing values (if any)
features = features.fillna(features.mean())

# Step 2: Encode categorical variables (if any)
label_encoder = LabelEncoder()
for column in features.select_dtypes(include=['object']).columns:
    features[column] = label_encoder.fit_transform(features[column])

# Step 3: Normalize numerical features
scaler = StandardScaler()
normalized_features = pd.DataFrame(scaler.fit_transform(features), columns=features.columns)

# Extract the output column (assuming it is the first column)
output_column = df.iloc[:, 0]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(normalized_features, output_column, test_size=0.2, random_state=42)

# Create a logistic regression model
logreg_model = LogisticRegression()

# Train the model on the training set
logreg_model.fit(X_train, y_train)

# Make predictions on the testing set
predictions = logreg_model.predict(X_test)

# Calculate and display the metrics as percentages
accuracy = accuracy_score(y_test, predictions) * 100
print("Accuracy of the Logistic Regression model: {:.2f}%".format(accuracy), "\n")

mse = mean_squared_error(y_test, predictions)
print("Mean squared error of the Logistic Regression model: {:.2f}%".format(mse), "\n")

mae = mean_absolute_error(y_test, predictions)
print("Mean absolute error of the Logistic Regression model: {:.2f}%".format(mae), "\n")

# Update with average='weighted' for multiclass targets
recall = recall_score(y_test, predictions, average='weighted') * 100
print("Recall of the Logistic Regression model: {:.2f}%".format(recall), "\n")

# Update with average='weighted' for multiclass targets
precision = precision_score(y_test, predictions, average='weighted') * 100
print("Precision of the Logistic Regression model: {:.2f}%".format(precision), "\n")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error, recall_score, precision_score

# Load the Excel file
file_path = "Kamalgera.xlsx"  # Replace with your file path
data = pd.read_excel(file_path)

# Separate input features (from the second to the last column) and output variable (first column)
X = data.iloc[:, 0:]
y = data.iloc[:, 0]

# Step 1: Separate numeric and non-numeric columns
numeric_cols = X.select_dtypes(include=['number']).columns
non_numeric_cols = X.select_dtypes(exclude=['number']).columns

# Step 2: Handle missing values using SimpleImputer with different strategies for numeric and non-numeric columns
imputer_numeric = SimpleImputer(strategy='mean')
imputer_non_numeric = SimpleImputer(strategy='most_frequent')

X_numeric = pd.DataFrame(imputer_numeric.fit_transform(X[numeric_cols]), columns=numeric_cols)
X_non_numeric = pd.DataFrame(imputer_non_numeric.fit_transform(X[non_numeric_cols]), columns=non_numeric_cols)

# Combine the numeric and non-numeric columns
X = pd.concat([X_numeric, X_non_numeric], axis=1)

# Step 3: Normalize input features using StandardScaler
scaler = StandardScaler()
X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

# Step 4: Encode non-numeric data using LabelEncoder
label_encoder = LabelEncoder()

for column in non_numeric_cols:
    X[column] = label_encoder.fit_transform(X[column])

# Step 5: Create a Naive Bayes model (Gaussian Naive Bayes for continuous features)
model = Pipeline([
    ('classifier', GaussianNB())
])

# Step 6: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Train the model
model.fit(X_train, y_train)

# Step 8: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 9: Display the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Naive Bayes Model Accuracy: {accuracy * 100:.2f}%","\n")

mse = mean_squared_error(y_test, y_pred)
print("Mean squared error of the Naive Bayes model: {:.2f}%".format(mse),"\n")

mae = mean_absolute_error(y_test, y_pred)
print("Mean absolute error of the Naive Bayes model: {:.2f}%".format(mae),"\n")

recall = recall_score(y_test, y_pred, average='weighted') * 100
print("Recall of the Naive Bayes model: {:.2f}%".format(recall),"\n")

precision = precision_score(y_test, y_pred, average='weighted') * 100
print("Precision of the Naive Bayes model: {:.2f}%".format(precision),"\n")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error, recall_score, precision_score

# Load the dataset
file_path = "Kamalgera.xlsx"
df = pd.read_excel(file_path)

# Extract the features (from the second column to the last)
X = df.iloc[:, 0:]

# Extract the output column (assuming it is the first column)
y = df.iloc[:, 0]

# Step 1: Handle missing values (if any)
X = X.fillna(X.mean())

# Step 2: Encode categorical variables (if any)
label_encoder = LabelEncoder()

for column in X.select_dtypes(include=['object']).columns:
    X[column] = label_encoder.fit_transform(X[column])

# Step 3: Normalize numerical features
scaler = StandardScaler()
X_normalized = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=42)

# Create an SVR model
svr_model = SVR()

# Train the model on the training set
svr_model.fit(X_train, y_train)

# Make predictions on the testing set
predictions = svr_model.predict(X_test)

# Calculate and display the accuracy of the model (using Mean Squared Error as an example)
mse = mean_squared_error(y_test, predictions)
accuracy = 1 - mse / y_test.var()
print("Accuracy of the SVR model: {:.2f}%".format(accuracy * 100),"\n")

print("Mean squared error of the SVR model: {:.2f}%".format(mse),"\n")

mae = mean_absolute_error(y_test, predictions)
print("Mean absolute error of the SVR model: {:.2f}%".format(mae),"\n")

recall = recall_score(y_test, predictions.round(), average='weighted') * 100
print("Recall of the SVR model: {:.2f}%".format(recall),"\n")

precision = precision_score(y_test, predictions.round(), average='weighted') * 100
print("Precision of the SVR model: {:.2f}%".format(precision),"\n")

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error, recall_score, precision_score
from sklearn.metrics import mean_squared_error

# Load the dataset
file_path = "Kamalgera.xlsx"
df = pd.read_excel(file_path)

# Extract the features (from the second to last column)
X = df.iloc[:, 0:]

# Extract the output column (first column)
y = df.iloc[:, 0]

# Step 1: Handle missing values (if any)
X = X.fillna(X.mean())

# Step 2: Encode categorical variables (if any)
label_encoder = LabelEncoder()

for column in X.select_dtypes(include=['object']).columns:
    X[column] = label_encoder.fit_transform(X[column])

# Step 3: Normalize numerical features
scaler = StandardScaler()
normalized_features = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(normalized_features, y, test_size=0.2, random_state=42)

# Apply Polynomial Regression
degree = 2
poly = PolynomialFeatures(degree=degree)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Create a Linear Regression model
poly_model = LinearRegression()

# Train the model on the polynomial features
poly_model.fit(X_train_poly, y_train)

# Make predictions on the testing set
predictions = poly_model.predict(X_test_poly)

# Calculate and display the R-squared score
mse = mean_squared_error(y_test, predictions)
accuracy = 1 - mse / y_test.var()

print("Accuracy of the Polynomial model: {:.2f}%".format(accuracy * 100),"\n")

print("Mean squared error of the Polynomial model: {:.2f}%".format(mse),"\n")

mae = mean_absolute_error(y_test, predictions)
print("Mean absolute error of the Polynomial model: {:.2f}%".format(mae),"\n")

recall = recall_score(y_test, predictions.round(), average='weighted') * 100
print("Recall of the Polynomial model: {:.2f}%".format(recall),"\n")

precision = precision_score(y_test, predictions.round(), average='weighted') * 100
print("Precision of the Polynomial model: {:.2f}%".format(precision),"\n")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error, recall_score, precision_score

# Load the dataset
file_path = "Kamalgera.xlsx"
df = pd.read_excel(file_path)

# Extract the features (from the third column to the last)
features = df.iloc[:, 1:]  # Assuming the first column is the target variable
output_column = df.iloc[:, 0]

# Step 1: Handle missing values (if any)
features = features.fillna(features.mean())

# Step 2: Encode categorical variables (if any)
label_encoder = LabelEncoder()
for column in features.select_dtypes(include=['object']).columns:
    features[column] = label_encoder.fit_transform(features[column])

# Step 3: Normalize numerical features
scaler = StandardScaler()
normalized_features = pd.DataFrame(scaler.fit_transform(features), columns=features.columns)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(normalized_features, output_column, test_size=0.2, random_state=42)

# Create a decision tree model
dt_model = DecisionTreeClassifier()

# Train the decision tree model on the training set
dt_model.fit(X_train, y_train)

# Make predictions on the testing set using decision tree
dt_predictions = dt_model.predict(X_test)

# Evaluate decision tree model
dt_accuracy = accuracy_score(y_test, dt_predictions) * 100
print("Accuracy of the Decision Tree model: {:.2f}%".format(dt_accuracy), "\n")

dt_mse = mean_squared_error(y_test, dt_predictions)
print("Mean squared error of the Decision Tree model: {:.2f}%".format(dt_mse), "\n")

dt_mae = mean_absolute_error(y_test, dt_predictions)
print("Mean absolute error of the Decision Tree model: {:.2f}%".format(dt_mae), "\n")

dt_recall = recall_score(y_test, dt_predictions, average='weighted') * 100
print("Recall of the Decision Tree model: {:.2f}%".format(dt_recall), "\n")

dt_precision = precision_score(y_test, dt_predictions, average='weighted') * 100
print("Precision of the Decision Tree model: {:.2f}%".format(dt_precision), "\n")

import matplotlib.pyplot as plt

# Performance criteria and their corresponding values
performance_criteria = ['accuracy_score', 'precision', 'recall', 'mae', 'mean_squared_error']
values = [57.14, 51.19, 57.14, 3.57, 35.71]

# Create a bar graph
plt.bar(performance_criteria, values)

# Add labels and title
plt.xlabel('Performance Criteria')
plt.ylabel('Percentage')
plt.title('Performance Evaluation of Logistic Regression')

# Display the graph
plt.show()

import matplotlib.pyplot as plt

# Performance criteria and their corresponding values
performance_criteria = ['accuracy_score', 'precision', 'recall', 'mae', 'mean_squared_error']
values = [78.57, 79.76, 78.57, 1.07, 5.36]

# Create a bar graph
plt.bar(performance_criteria, values)

# Add labels and title
plt.xlabel('Performance Criteria')
plt.ylabel('Percentage')
plt.title('Performance Evaluation of Naive Bayes')

# Display the graph
plt.show()

import matplotlib.pyplot as plt

# Performance criteria and their corresponding values
performance_criteria = ['accuracy_score', 'precision', 'recall', 'mae', 'mean_squared_error']
values = [30.94, 1.79, 7.14, 6.54, 62.23]

# Create a bar graph
plt.bar(performance_criteria, values)

# Add labels and title
plt.xlabel('Performance Criteria')
plt.ylabel('Percentage')
plt.title('Performance Evaluation of SVR')

# Display the graph
plt.show()

import matplotlib.pyplot as plt

# Performance criteria and their corresponding values
performance_criteria = ['accuracy_score', 'precision', 'recall', 'mae', 'mean_squared_error']
values = [48.36, 14.29, 7.14, 4.65, 46.53]

# Create a bar graph
plt.bar(performance_criteria, values)

# Add labels and title
plt.xlabel('Performance Criteria')
plt.ylabel('Percentage')
plt.title('Performance Evaluation of Polynomial Regression')

# Display the graph
plt.show()

import matplotlib.pyplot as plt

# Performance criteria and their corresponding values
performance_criteria = ['accuracy_score', 'precision', 'recall', 'mae', 'mean_squared_error']
values = [21.43, 26.19, 21.43, 6.43, 67.86]

# Create a bar graph
plt.bar(performance_criteria, values)

# Add labels and title
plt.xlabel('Performance Criteria')
plt.ylabel('Percentage')
plt.title('Performance Evaluation of Decision Tree')

# Display the graph
plt.show()