import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error


N = int(input("Enter the number of points (N): "))
k = int(input("Enter the number of neighbors (k): "))


x_values = []
y_values = []

for i in range(N):
    x = float(input(f"Enter x value for point {i+1}: "))
    y = float(input(f"Enter y value for point {i+1}: "))
    x_values.append(x)
    y_values.append(y)


X_train = np.array(x_values).reshape(-1, 1)
y_train = np.array(y_values)


X_new = float(input("Enter the value of X to predict Y: "))
X_new = np.array([[X_new]])


if k > N:
    print("Error: k should be less than or equal to N.")
else:
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)
    
 
    y_pred = model.predict(X_new)
    print(f"The predicted Y value for X = {X_new[0][0]} is: {y_pred[0]}")
    
   
    variance = np.var(y_train)
    print(f"Variance of the labels: {variance}")
