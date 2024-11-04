import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

#creating a synthetic dataset
np.random.seed(42)

data = {
    'customer_id': range(1,1001),
    'age': np.random.randint(18, 70, size=1000),
    'tenure': np.random.randint(1, 48, size=1000),  # Tenure in months
    'monthly_charges': np.random.uniform(10, 100, size=1000),
    'total_charges': np.random.uniform(100, 4000, size=1000),
    'customer_support_calls': np.random.randint(0, 10, size=1000),
    'churn': np.random.choice([0, 1], size=1000, p=[0.7, 0.3])  # 30% churn rate
}

df = pd.DataFrame(data)
print(df.head)

# Check for missing values
print(df.isnull().sum())

# Convert 'total_charges' to numeric (if needed)
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')

# Drop rows with missing values (if any)
df.dropna(inplace=True)

# Features and target variable
X = df.drop(['customer_id', 'churn'], axis=1)
y = df['churn']

# Visualizing churn distribution
sns.countplot(x='churn', data=df)
plt.title('Customer Churn Distribution')
plt.show()

# Correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Confusion matrix
confusion = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:\n', confusion)

# Classification report
report = classification_report(y_test, y_pred)
print('Classification Report:\n', report)

# Feature importance
importances = model.feature_importances_
feature_names = X.columns
indices = np.argsort(importances)[::-1]

# Plotting feature importances
plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), feature_names[indices], rotation=90)
plt.xlim([-1, X.shape[1]])
plt.show()
