# Step 1: Import required libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# Step 2: Create a sample dataset
data = {
'Area': [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700],
'Price': [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
}
df = pd.DataFrame(data)
# Step 3: Split features and target
X = df[['Area']] # Independent variable
y = df['Price'] # Dependent variable
# Step 4: Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)
# Step 5: Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Step 6: Predict house prices
y_pred = model.predict(X_test)
# Step 7: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)
# Step 8: Predict price for a new house area
new_area = np.array([[1800]])
predicted_price = model.predict(new_area)
print("Predicted House Price for 1800 sq.ft:", predicted_price[0])