import random
import math

def change_into_qubit(vector):
    # input: qubit输出的概率比例值 
    # output: 符合qubit state要求的状态向量
    vector=[pow(i, 0.5) for i in vector]
    length=len(vector)
    while length%2 != 1:
        length/=2
    if length != 1:
        return ('wrong vector')
    
    whole=0
    for i in vector:
        whole+= i * i.conjugate()
    
    return [x/pow(whole,0.5) for x in vector]

def UU_CNOT_UU(u1, u2, u3, u4):
    # input: 
    # U1-x-U3
    # U2-N-U4
    # output: get the probability of four U gates
    [a,b],[c,d],[e,f],[g,h]=u1,u2,u3,u4
    p,q,r,m=a*c,a*d,b*d,b*c
    x1,x2,x3,x4=p*e-r*f, q*e-m*f, p*f+r*e, q*f+m*e
    y1,y2,y3,y4=x1*g-x2*h, x1*h+x2*g, x3*g-x4*h, x3*h+x4*g
    vector=np.array([y1,y2,y3,y4])
    prob=pow(vector,2)
    return prob

def UU_NOTC_UU(u1, u2, u3, u4):
    # input: 
    # U1-N-U3
    # U2-x-U4
    # output: get the probability of four U gates
    [a,b],[c,d],[e,f],[g,h]=u1,u2,u3,u4
    p,q,r,m=a*c,a*d,b*d,b*c
    x1,x2,x3,x4=p*e-r*f, q*e-m*f, p*f+r*e, q*f+m*e
    y1,y3,y2,y4=x1*g-x2*h, x1*h+x2*g, x3*g-x4*h, x3*h+x4*g
    vector=np.array([y1,y2,y3,y4])
    prob=pow(vector,2)
    return prob

def u3_calculator(start_state, final_state):
    # input: 单个qubit的输入状态向量和目标的输出状态向量
    # output: U-gate转化的角度
    [a,b],[x,y]=start_state, final_state
    if b==0:
        theta=2*math.acos(x.real)
        exp_i_fi = y/(abs(y))
        fi=math.atan((exp_i_fi.imag)/(exp_i_fi.real))
        lamb=0.0
    else:
        lamb=-math.atan((b.imag)/(b.real))
        theta=2*(math.asin(x.real)-math.acos(a.real))
        exp_i_fi = y/(abs(y))
        fi=math.atan((exp_i_fi.imag)/(exp_i_fi.real))
        return theta, fi, lamb

def UU_Cal():
    # for a single U gate
    random_value_1 = random.randint(1,9)
    random_value_2 = 10 - random_value_1
    # start_state = change_into_qubit([1,1])
    start_1 = complex(random_value_2, random.randint(0,1))
    start_2 = complex(random_value_1, random.randint(0,1))
    final_1 = complex(random_value_1, random.randint(0,1))
    final_2 = complex(random_value_2, random.randint(0,1))
    start_state = change_into_qubit([start_1, start_2])
    final_state = change_into_qubit([final_1, final_2])
    theta, fi, lamb = u3_calculator(start_state, final_state)
    return theta * 100, fi * 80, lamb * 50
