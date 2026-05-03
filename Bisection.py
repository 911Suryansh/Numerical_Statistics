def bisection(  f ,a , b ,tol , itr):
    if  f(a) * f(b) >= 0:
        print("interval is wrong must be possitive")
        return None

    for i  in range(itr):
        c = (a+b)/2
        print(f"{i+1}\t {a : .6f}\t {b : .6f}\t {f(c) : .6f}")


        if abs(f(c)) < tol or b -a < tol:
            return c

        if f(a) * f(c) > 0:
            a = c
        else:
            b =c


    return c          





def f(x):
    return x**3 -x -2


a = 1 
b = 2
tol = 0.001
itr = 10
output = bisection( f, a , b, tol , itr)
print(f"approx root : {output} ")

    