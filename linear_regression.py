import numpy as np

class LinearRegression:


    def __init__(self):
        pass
    
    def fit(self,X, y, rate = 0.01, epochs = 1000):
        
        features, n = X.shape

        self.coeff_ = [1 for i in range(features)]


        for _ in range(100):
            y_pred = np.dot(np.array(X[:features - 1]) , X).T + self.coeff_[features -1 ]

            cost = (1/n)*(np.sum((y_pred-y)*2))

            #print(cost)

            for i in range(features - 1):

                self.coeff_[i] = self.coeff_[i] - 2*(rate/n)*(np.sum(np.dot((y_pred-y).T,X[i])))

            self.coeff_[features - 1] = self.coeff_[features -1 ] - 2*(rate/n)*(np.sum(y_pred - y))
        

    def score(self,X, y):
        pass

    def predict(self,X):
        pass

