def gauss_seidal( itr , tol):
    x , y , z = 0 , 0 , 0

    for i in range(itr):
        x_old , y_old , z_old = x , y, z

        x =  ( 6 - y - z)/2
        y = ( 2 - x+ z)/3
        z = ( 3 - x+ y )/2

        print(f"{i+1}\t {x : .6f}\t {y : .6f}\t {z: .6f}")

        if abs(  x -x_old)  < tol and abs( y - y_old) < tol and abs(z- z_old) < tol:
            print("converged")
            return  x , y, z
        
    return x , y, z



itr = 10
tol = 0.001
root = gauss_seidal( itr , tol)
print(f"root : { root}")