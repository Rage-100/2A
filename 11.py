import numpy as np 
X = np.array([1,2,3,4,5]) 
y = np.array([2,4,6,8,10]) 
m, c = 0.0, 0.0 
lr, epochs = 0.01, 1000 
n = len(X) 
for i in range(epochs): 
    y_pred = m*X + c 
    m -= lr * (-2/n) * np.sum(X * (y - y_pred)) 
    c -= lr * (-2/n) * np.sum(y - y_pred) 
    if i % 200 == 0: 
        print(f"Epoch {i}, Loss = {np.mean((y - y_pred)**2):.4f}") 
print(f"\nFinal parameters: \nSlope (m)={m:.2f}, \nIntercept (c)={c:.2f}")
