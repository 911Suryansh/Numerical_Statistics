def newton_forward(x, y, value):
    n = len(x)
    

    diff = [y.copy()]
    
    for i in range(1, n):
        temp = []
        for j in range(n - i):
            temp.append(diff[i-1][j+1] - diff[i-1][j])
        diff.append(temp)
    
  
    h = x[1] - x[0]  
    p= (value - x[0]) / h
    
  
    result = y[0]
    term = 1
    
    for i in range(1, n):
        term *= (p - (i - 1)) / i
        result += term * diff[i][0]
    
    return result



x = [0, 1, 2, 3]
y = [1, 2, 4, 8]

value = 1.8

result = newton_forward(x, y, value)
print("Interpolated value:", result)