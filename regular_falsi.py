def regular_falsi( a , b, tol , itr , f):
    if f(a) * f(b) >= 0 :
        print("wrong interval")
        return None
    for i in range(itr):
        c = ( a * f(b) - b * f(a) ) / (f(b)-f(  a))
        print(f"{i+1}\t {a : .6f}\t {b : .6f}\t {f(c) : .6f}")

        if abs(f(c)) < tol :
            return c
        
        if f(a) * f(c) > 0:
            a = c
        else:
            b = c

    return c    






def f(x):
    return x**3 -x -2



a  =  1
b = 2
tol = 0.001
itr  =10
root = regular_falsi( a , b , tol , itr, f)
print( f" approx root : { root}")
