import numpy as np
import matplotlib.pyplot as plt

####### (distance = 1) #######
print(' ')
print('DISTANCE = 1')
print(' ')
# set node distance matrix 
x0,x1,x2,x3 = 0,1,2,3
node_matrix1 = np.matrix([[x0],[x1],[x2],[x3]])

# for variable cross-sectional area
A0,A1,A2,A3 = 1-float(x0)/6,1-float(x1)/6,1-float(x2)/6,1-float(x3)/6
area_matrix = np.matrix([[A0],[A1],[A2],[A3]])
print(' area_matrix = ')
print(area_matrix)

# set initial matrix from equations
e1 = np.matrix([[-A0,A1],[0,0]])
e2 = np.matrix([[-A1,A2],[0,0]])
e3 = np.matrix([[-A2,A3],[0,0]])

print('e1 = ')
print(e1)
print('e2 = ')
print(e2)
print('e3 = ')
print(e3)

# set global matric from local values
global_matrix = np.matrix([[e1.item((0,0)),e1.item((0,1)),0,0],
                           [e1.item((1,0)),e1.item((1,1))+e2.item((0,0)),e2.item((0,1)),0],
                           [0,e2.item((1,0)),e2.item((1,1))+e3.item((0,0)),e3.item((1,0))],
                           [0,0,e3.item((1,0)),e3.item((1,1))]])               

print('global_matrix = ')
print(global_matrix)

# set variables matrix
v0 = 3
v1,v2,v3 = 0,0,0
Q0, Q1, Q2, Q3 = 1, 1, 1, 1

vel_matrix = np.matrix([[v0],[v1],[v2],[v3]])
flux_matrix = np.matrix([[Q0],[Q1],[Q2],[Q3]])

# use initial condition for v0=3
global_matrix = np.matrix([[e1.item((0,1)),0,0],
                           [e1.item((1,1))+e2.item((0,0)),e2.item((0,1)),0],
                           [e2.item((1,0)),e2.item((1,1))+e3.item((0,0)),e3.item((0,1))]])               
print('global_matrix = ')
print(global_matrix)

inv_global_matrix = np.linalg.inv(global_matrix)
print('inv_global_matrix = ')
print(inv_global_matrix)

# solve for velocity
Q1 = -e1.item((0,0))*v0+1
flux_matrix = np.matrix([[Q1],[Q2],[Q3]])
vel_matrix = np.matmul(inv_global_matrix,flux_matrix)
print('vel_matrix = ')
print(vel_matrix)

# analytical solution
vel_matrix_exact = -6*np.log(area_matrix)+3
print('vel_matrix_exact = ')
print(vel_matrix_exact)

# error E
E_matrix1 = np.zeros((3,1))
for i in range(0,3):
    E_matrix1[i] = vel_matrix[i]-vel_matrix_exact[i+1]
print('E_matrix1 = ')
print(E_matrix1)

####### (distance = 0.5) #######
print(' ')
print('DISTANCE = 0.5')
print(' ')
# set node distance matrix 
x0,x1,x2,x3,x4,x5,x6 = 0,0.5,1,1.5,2,2.5,3
node_matrix05 = np.matrix([[x0],[x1],[x2],[x3],[x4],[x5],[x6]])

# for variable cross-sectional area
A0,A1,A2,A3,A4,A5,A6 = 1-float(x0)/6,1-float(x1)/6,1-float(x2)/6,1-float(x3)/6,1-float(x4)/6,1-float(x5)/6,1-float(x6)/6
area_matrix = np.matrix([[A0],[A1],[A2],[A3],[A4],[A5],[A6]])
print(' area_matrix = ')
print(area_matrix)

# set initial matrix from equations
e1 = np.matrix([[-A0,A1],[0,0]])/(x1-x0)
e2 = np.matrix([[-A1,A2],[0,0]])/(x2-x1)
e3 = np.matrix([[-A2,A3],[0,0]])/(x3-x2)
e4 = np.matrix([[-A3,A4],[0,0]])/(x4-x3)
e5 = np.matrix([[-A4,A5],[0,0]])/(x5-x4)
e6 = np.matrix([[-A5,A6],[0,0]])/(x6-x5)

print('e1 = ')
print(e1)
print('e2 = ')
print(e2)
print('e3 = ')
print(e3)
print('e4 = ')
print(e4)
print('e5 = ')
print(e5)
print('e6 = ')
print(e6)

# set global matric from local values
global_matrix = np.matrix([[e1.item((0,0)),e1.item((0,1)),0,0,0,0,0],
                           [e1.item((1,0)),e1.item((1,1))+e2.item((0,0)),e2.item((0,1)),0,0,0,0],
                           [0,e2.item((1,0)),e2.item((1,1))+e3.item((0,0)),e3.item((0,1)),0,0,0],
                           [0,0,e3.item((1,0)),e3.item((1,1))+e4.item((0,0)),e4.item((0,1)),0,0],
                           [0,0,0,e4.item((1,0)),e4.item((1,1))+e5.item((0,0)),e5.item((0,1)),0],
                           [0,0,0,0,e5.item((1,0)),e5.item((1,1))+e6.item((0,0)),e6.item((0,1))],
                           [0,0,0,0,0,e6.item((1,0)),e6.item((1,1))]])               

print('global_matrix = ')
print(global_matrix)

# set variables matrix
v0 = 3
v1,v2,v3,v4,v5,v6 = 0,0,0,0,0,0
Q0,Q1, Q2, Q3, Q4,Q5,Q6 = 1,1,1,1,1,1,1

vel_matrix = np.matrix([[v0],[v1],[v2],[v3],[v4],[v5],[v6]])
flux_matrix = np.matrix([[Q0],[Q1],[Q2],[Q3],[Q4],[Q5],[Q6]])

# use initial condition for v0=3
global_matrix = np.matrix([[e1.item((0,1)),0,0,0,0,0],
                           [e1.item((1,1))+e2.item((0,0)),e2.item((0,1)),0,0,0,0],
                           [e2.item((1,0)),e2.item((1,1))+e3.item((0,0)),e3.item((0,1)),0,0,0],
                           [0,e3.item((1,0)),e3.item((1,1))+e4.item((0,0)),e4.item((0,1)),0,0],
                           [0,0,e4.item((1,0)),e4.item((1,1))+e5.item((0,0)),e5.item((0,1)),0],
                           [0,0,0,e5.item((1,0)),e5.item((1,1))+e6.item((0,0)),e6.item((0,1))]])

print('global_matrix = ')
print(global_matrix)

inv_global_matrix = np.linalg.inv(global_matrix)
print('inv_global_matrix = ')
print(inv_global_matrix)

# solve for velocity
Q1 = -e1.item((0,0))*v0+1
flux_matrix = np.matrix([[Q1],[Q2],[Q3],[Q4],[Q5],[Q6]])
vel_matrix = np.matmul(inv_global_matrix,flux_matrix)
print('vel_matrix = ')
print(vel_matrix)

# analytical solution
vel_matrix_exact = -6*np.log(area_matrix)+3
print('vel_matrix_exact = ')
print(vel_matrix_exact)

# error E
E_matrix05 = np.zeros((6,1))
for i in range(0,6):
    E_matrix05[i] = vel_matrix[i]-vel_matrix_exact[i+1]
print('E_matrix05 = ')
print(E_matrix05)

####### (distance = 0.25) #######
print(' ')
print('DISTANCE = 0.25')
print(' ')
# set node distance matrix 
x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12 = 0,0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3
node_matrix025 = np.matrix([[x0],[x1],[x2],[x3],[x4],[x5],[x6],[x7],[x8],[x9],[x10],[x11],[x12]])

# for variable cross-sectional area
A0,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12 = 1-float(x0)/6,1-float(x1)/6,1-float(x2)/6,1-float(x3)/6,1-float(x4)/6,1-float(x5)/6,1-float(x6)/6,1-float(x7)/6,1-float(x8)/6,1-float(x9)/6,1-float(x10)/6,1-float(x11)/6,1-float(x12)/6
area_matrix = np.matrix([[A0],[A1],[A2],[A3],[A4],[A5],[A6],[A7],[A8],[A9],[A10],[A11],[A12]])
print(' area_matrix = ')
print(area_matrix)

# set initial matrix from equations
e1 = np.matrix([[-A0,A1],[0,0]])/(x1-x0)
e2 = np.matrix([[-A1,A2],[0,0]])/(x2-x1)
e3 = np.matrix([[-A2,A3],[0,0]])/(x3-x2)
e4 = np.matrix([[-A3,A4],[0,0]])/(x4-x3)
e5 = np.matrix([[-A4,A5],[0,0]])/(x5-x4)
e6 = np.matrix([[-A5,A6],[0,0]])/(x6-x5)
e7 = np.matrix([[-A6,A7],[0,0]])/(x7-x6)
e8 = np.matrix([[-A7,A8],[0,0]])/(x8-x7)
e9 = np.matrix([[-A8,A9],[0,0]])/(x9-x8)
e10 = np.matrix([[-A9,A10],[0,0]])/(x10-x9)
e11 = np.matrix([[-A10,A11],[0,0]])/(x11-x10)
e12 = np.matrix([[-A11,A12],[0,0]])/(x12-x11)                         

print('e1 = ')
print(e1)
print('e2 = ')
print(e2)
print('e3 = ')
print(e3)
print('e4 = ')
print(e4)
print('e5 = ')
print(e5)
print('e6 = ')
print(e6)
print('e7 = ')
print(e7)
print('e8 = ')
print(e8)
print('e9 = ')
print(e9)
print('e10 = ')
print(e10)
print('e11 = ')
print(e11)
print('e12 = ')
print(e12)                         

# set global matric from local values
global_matrix = np.matrix([[e1.item((0,0)),e1.item((0,1)),0,0,0,0,0,0,0,0,0,0,0],
                           [e1.item((1,0)),e1.item((1,1))+e2.item((0,0)),e2.item((0,1)),0,0,0,0,0,0,0,0,0,0],
                           [0,e2.item((1,0)),e2.item((1,1))+e3.item((0,0)),e3.item((0,1)),0,0,0,0,0,0,0,0,0],
                           [0,0,e3.item((1,0)),e3.item((1,1))+e4.item((0,0)),e4.item((0,1)),0,0,0,0,0,0,0,0],
                           [0,0,0,e4.item((1,0)),e4.item((1,1))+e5.item((0,0)),e5.item((0,1)),0,0,0,0,0,0,0],
                           [0,0,0,0,e5.item((1,0)),e5.item((1,1))+e6.item((0,0)),e6.item((0,1)),0,0,0,0,0,0],
                           [0,0,0,0,0,e6.item((1,0)),e6.item((1,1))+e7.item((0,0)),e7.item((0,1)),0,0,0,0,0],
                           [0,0,0,0,0,0,e7.item((1,0)),e7.item((1,1))+e8.item((0,0)),e8.item((0,1)),0,0,0,0],
                           [0,0,0,0,0,0,0,e8.item((1,0)),e8.item((1,1))+e9.item((0,0)),e9.item((0,1)),0,0,0],
                           [0,0,0,0,0,0,0,0,e9.item((1,0)),e9.item((1,1))+e10.item((0,0)),e10.item((0,1)),0,0],
                           [0,0,0,0,0,0,0,0,0,e10.item((1,0)),e10.item((1,1))+e11.item((0,0)),e11.item((0,1)),0],
                           [0,0,0,0,0,0,0,0,0,0,e11.item((1,0)),e11.item((1,1))+e12.item((0,0)),e12.item((0,1))],
                           [0,0,0,0,0,0,0,0,0,0,0,e12.item((1,0)),e12.item((1,1))]])               

print('global_matrix = ')
print(global_matrix)

# set variables matrix
v0 = 3
v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12 = 0,0,0,0,0,0,0,0,0,0,0,0
Q0,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12 = 1,1,1,1,1,1,1,1,1,1,1,1,1

vel_matrix = np.matrix([[v0],[v1],[v2],[v3],[v4],[v5],[v6],[v7],[v8],[v9],[v10],[v11],[v12]])
flux_matrix = np.matrix([[Q0],[Q1],[Q2],[Q3],[Q4],[Q5],[Q6],[Q7],[Q8],[Q9],[Q10],[Q11],[Q12]])

# use initial condition for v0=3
global_matrix = np.matrix([[e1.item((0,1)),0,0,0,0,0,0,0,0,0,0,0],
                           [e1.item((1,1))+e2.item((0,0)),e2.item((0,1)),0,0,0,0,0,0,0,0,0,0],
                           [e2.item((1,0)),e2.item((1,1))+e3.item((0,0)),e3.item((0,1)),0,0,0,0,0,0,0,0,0],
                           [0,e3.item((1,0)),e3.item((1,1))+e4.item((0,0)),e4.item((0,1)),0,0,0,0,0,0,0,0],
                           [0,0,e4.item((1,0)),e4.item((1,1))+e5.item((0,0)),e5.item((0,1)),0,0,0,0,0,0,0],
                           [0,0,0,e5.item((1,0)),e5.item((1,1))+e6.item((0,0)),e6.item((0,1)),0,0,0,0,0,0],
                           [0,0,0,0,e6.item((1,0)),e6.item((1,1))+e7.item((0,0)),e7.item((0,1)),0,0,0,0,0],
                           [0,0,0,0,0,e7.item((1,0)),e7.item((1,1))+e8.item((0,0)),e8.item((0,1)),0,0,0,0],
                           [0,0,0,0,0,0,e8.item((1,0)),e8.item((1,1))+e9.item((0,0)),e9.item((0,1)),0,0,0],
                           [0,0,0,0,0,0,0,e9.item((1,0)),e9.item((1,1))+e10.item((0,0)),e10.item((0,1)),0,0],
                           [0,0,0,0,0,0,0,0,e10.item((1,0)),e10.item((1,1))+e11.item((0,0)),e11.item((0,1)),0],
                           [0,0,0,0,0,0,0,0,0,e11.item((1,0)),e11.item((1,1))+e12.item((0,0)),e12.item((0,1))]])   

print('global_matrix = ')
print(global_matrix)

inv_global_matrix = np.linalg.inv(global_matrix)
print('inv_global_matrix = ')
print(inv_global_matrix)

# solve for velocity
Q1 = -e1.item((0,0))*v0+1
flux_matrix = np.matrix([[Q1],[Q2],[Q3],[Q4],[Q5],[Q6],[Q7],[Q8],[Q9],[Q10],[Q11],[Q12]])
vel_matrix = np.matmul(inv_global_matrix,flux_matrix)
print('vel_matrix = ')
print(vel_matrix)

# analytical solution
vel_matrix_exact = -6*np.log(area_matrix)+3
print('vel_matrix_exact = ')
print(vel_matrix_exact)

# error E
E_matrix025 = np.zeros((12,1))
for i in range(0,12):
    E_matrix025[i] = vel_matrix[i]-vel_matrix_exact[i+1]
print('E_matrix025 = ')
print(E_matrix025)

### loglog plot ###

plt.figure()
plt.loglog(node_matrix1,E_matrix1)
plt.show()

