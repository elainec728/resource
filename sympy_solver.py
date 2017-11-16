# # coding:utf-8

from sympy import *

b0,b1,b2,b3 = symbols('b0,b1,b2,b3')
x1,x2,x3,x4,y1,y2,y3,y4 = symbols('x1,x2,x3,x4,y1,y2,y3,y4')

# eqns =[b0 + b1 * x1 + b2 * x1 ** 2 + b3 * x1 ** 3 - y1,
#        b0 + b1 * x1 + b2 * x1 ** 2 + b3 * x1 ** 3 - y2,
#        b0 + b1 * x1 + b2 * x1 ** 2 + b3 * x1 ** 3 - y3,
#        b0 + b1 * x1 + b2 * x1 ** 2 + b3 * x1 ** 3 - y4]

#solver
A = Matrix([[1,x1, x1**2, x1**3], [1,x2, x2**2, x2**3], [1,x3, x3**2, x3**3], [1,x4, x4**2, x4**3]])
b = Matrix([y1, y2, y3, y4])
para=list(linsolve((A, b), [b0,b1,b2,b3]))

para0=para[0][0]
para1=para[0][1]
para2=para[0][2]
para3=para[0][3]

print(para0)
print(para1)
print(para2)
print(para3)

#testing
def calc_para(para):
    str_expr = str(para)
    expr = sympify(str_expr)
    return expr.subs([(x1,0),(x2,89),(x3,181),(x4,272),(y1,5422.3999939),(y2,5504.6999969),(y3,5570.5921567),(y4,5557.5)])

b0=calc_para(para0)
b1=calc_para(para1)
b2=calc_para(para2)
b3=calc_para(para3)

print(b0)
print(b1)
print(b2)
print(b3)

'''
(-x1*(((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*((x1 - x2)*(y1 - y4) - (x1 - x4)*(y1 - y2)) - ((x1 - x2)*(x1**2 - x4**2) - (x1 - x4)*(x1**2 - x2**2))*((x1 - x2)*(y1 - y3) - (x1 - x3)*(y1 - y2)))*(-((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*(x1**3 + x1**2*(-x1 + x2) - x2**3) + ((x1 - x2)*(x1**3 - x3**3) - (x1 - x3)*(x1**3 - x2**3))*(x1**2 + x1*(-x1 + x2) - x2**2)) + (((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x4**3) - (x1 - x4)*(x1**3 - x2**3)) - ((x1 - x2)*(x1**2 - x4**2) - (x1 - x4)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x3**3) - (x1 - x3)*(x1**3 - x2**3)))*(x1*((x1 - x2)*(y1 - y3) - (x1 - x3)*(y1 - y2))*(x1**2 + x1*(-x1 + x2) - x2**2) + (x1*(-y1 + y2) - y1*(-x1 + x2))*((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))))/((x1 - x2)*((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*(((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x4**3) - (x1 - x4)*(x1**3 - x2**3)) - ((x1 - x2)*(x1**2 - x4**2) - (x1 - x4)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x3**3) - (x1 - x3)*(x1**3 - x2**3))))
(-((-x1**2 + x2**2)*((-x1 + x2)*(-x1**3 + x3**3) - (-x1 + x3)*(-x1**3 + x2**3)) - (-x1**3 + x2**3)*((-x1 + x2)*(-x1**2 + x3**2) - (-x1 + x3)*(-x1**2 + x2**2)))*(((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*((x1 - x2)*(y1 - y4) - (x1 - x4)*(y1 - y2)) - ((x1 - x2)*(x1**2 - x4**2) - (x1 - x4)*(x1**2 - x2**2))*((x1 - x2)*(y1 - y3) - (x1 - x3)*(y1 - y2))) + ((-x1**2 + x2**2)*((-x1 + x2)*(-y1 + y3) - (-x1 + x3)*(-y1 + y2)) - (-y1 + y2)*((-x1 + x2)*(-x1**2 + x3**2) - (-x1 + x3)*(-x1**2 + x2**2)))*(((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x4**3) - (x1 - x4)*(x1**3 - x2**3)) - ((x1 - x2)*(x1**2 - x4**2) - (x1 - x4)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x3**3) - (x1 - x3)*(x1**3 - x2**3))))/((x1 - x2)*((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*(((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x4**3) - (x1 - x4)*(x1**3 - x2**3)) - ((x1 - x2)*(x1**2 - x4**2) - (x1 - x4)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x3**3) - (x1 - x3)*(x1**3 - x2**3))))
(-((x1 - x2)*(x1**3 - x3**3) - (x1 - x3)*(x1**3 - x2**3))*(((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*((x1 - x2)*(y1 - y4) - (x1 - x4)*(y1 - y2)) - ((x1 - x2)*(x1**2 - x4**2) - (x1 - x4)*(x1**2 - x2**2))*((x1 - x2)*(y1 - y3) - (x1 - x3)*(y1 - y2))) + ((x1 - x2)*(y1 - y3) - (x1 - x3)*(y1 - y2))*(((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x4**3) - (x1 - x4)*(x1**3 - x2**3)) - ((x1 - x2)*(x1**2 - x4**2) - (x1 - x4)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x3**3) - (x1 - x3)*(x1**3 - x2**3))))/(((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*(((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x4**3) - (x1 - x4)*(x1**3 - x2**3)) - ((x1 - x2)*(x1**2 - x4**2) - (x1 - x4)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x3**3) - (x1 - x3)*(x1**3 - x2**3))))
(((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*((x1 - x2)*(y1 - y4) - (x1 - x4)*(y1 - y2)) - ((x1 - x2)*(x1**2 - x4**2) - (x1 - x4)*(x1**2 - x2**2))*((x1 - x2)*(y1 - y3) - (x1 - x3)*(y1 - y2)))/(((x1 - x2)*(x1**2 - x3**2) - (x1 - x3)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x4**3) - (x1 - x4)*(x1**3 - x2**3)) - ((x1 - x2)*(x1**2 - x4**2) - (x1 - x4)*(x1**2 - x2**2))*((x1 - x2)*(x1**3 - x3**3) - (x1 - x3)*(x1**3 - x2**3)))
5422.39999390000
0.817113187731877
0.00236998403719996
-1.30441399079980e-5
'''
