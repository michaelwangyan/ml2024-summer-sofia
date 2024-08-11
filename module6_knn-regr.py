import numpy as np


class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.x_values = []
        self.y_values = []

    def add_point(self, x, y):
        self.x_values.append(x)
        self.y_values.append(y)

    def predict(self, x):
        distances = []
        for i in range(len(self.x_values)):
            dist = abs(self.x_values[i] - x)
            distances.append((dist, self.y_values[i]))

      
        distances.sort()
        nearest_neighbors = distances[:self.k]
        
    
        y_pred = np.mean([y for _, y in nearest_neighbors])
        return y_pred


def main():
    N = int(input("Enter the number of points (N): "))
    k = int(input("Enter the value of k: "))

    if k > N:
        print("Error: k cannot be greater than N")
        return


    knn = KNNRegressor(k)

  
    for i in range(N):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))
        knn.add_point(x, y)


    x_to_predict = float(input("Enter the X value to predict: "))
    y_pred = knn.predict(x_to_predict)

    print(f"The predicted Y value for X = {x_to_predict} is {y_pred}")

if __name__ == "__main__":
    main()
