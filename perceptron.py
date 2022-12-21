import numpy as np

class Perceptron:
    def __init__(self,input_size,learning_rate = 0.3):
        self.weight = np.random.rand(input_size + 1)
        self.learning_rate = learning_rate
    
    def predict(self,x):
        x = np.append(x,1)
        output = np.dot(x,self.weight)
        return 1 if output >= 1 else 0
    
    def fit(self,x,y,epoch = 100):
        for _ in range(epoch):
            for xi,yi in zip(x,y):
                y_pred = self.predict(xi)
                if yi != y_pred:
                    xi = np.append(xi,1)
                    self.weight += self.learning_rate * (yi - y_pred)  * xi

X = np.array([[0,0],[0,1],[1,0],[1,1] ])
Y = np.array([0,1,1,0])

p = Perceptron(2)
p.fit(X,Y)

for x,y in zip(X,Y):
    y_pred = p.predict(x)
    print(f'input : {x} output: {y_pred} expected : {y} ')