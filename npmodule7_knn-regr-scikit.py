import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("That's not a valid number. Please enter a positive integer.")


def main():
    N = get_positive_integer("Enter the number of points (N): ")
    k = get_positive_integer("Enter the value of k: ")

    if k > N:
        print("Error: k cannot be greater than N")
        return

    x_values = []
    y_values = []

    
    for i in range(N):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))
        x_values.append([x])
        y_values.append(y)

    
    x_array = np.array(x_values)
    y_array = np.array(y_values)


    variance_y = np.var(y_array)
    print(f"Variance of y values: {variance_y}")


    x_to_predict = float(input("Enter the X value to predict: "))
    x_to_predict = np.array([[x_to_predict]])

   
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(x_array, y_array)
    y_pred = knn.predict(x_to_predict)

    print(f"The predicted Y value for X = {x_to_predict[0][0]} is {y_pred[0]}")

if __name__ == "__main__":
    main()
