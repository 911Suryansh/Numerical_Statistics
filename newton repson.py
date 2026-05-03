def f(x):
    return x**3 -x -2

def dx(x):
    return 3*x**2 - 1 


def newton_rephson( f , dx ,x0 , tol , itr):
    for i in range(itr):
        if dx(x0) == 0:
            print(" zero divison error...")
            return None
        
        x1 = x0 - f(x0)/dx(x0)
        print(f"{i+1}\t {x0 : .6f}\t {x1 : .6f}\t {f(x1): .6f}")

        if abs( x1 - x0) < tol :
            return x1
        
        x0 = x1
    return x1


x0 = 1.5
tol = 0.001
itr = 10
root = newton_rephson( f , dx , x0 , tol , itr)
print(f"approx root : {root}")
