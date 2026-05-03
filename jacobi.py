def jacobi( itr , tol ):
     x , y , z = 0 , 0 , 0

     for i in range(itr):
          x1  =  ( 4  - y  - z)/4
          y1 = ( 6 - x +z)/3
          z1 = ( 5 -x  -y) /1
           
          print(f"{i+1}\t {x : .6f}\t {y : .6f}\t {z: .6f}")

          if abs(x1 - x  ) < tol  and abs( y1 - y )<tol and abs(z1 -z) < tol:
               print("converged")
               return x1 ,y1, z1
          
          x , y , z  = x1 , y1 , z1
     return x1 , y1 , z1
     

itr  = 10 
tol = 0.001
root = jacobi( itr , tol)
print(f" approx root : { root}")    