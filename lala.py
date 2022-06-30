import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import optimize
    listc = [-600,-800,-500,-400,-300]
    A = [[1000,2000,0,0,0],[-1,-1,0,0,0] ,[1000,2000,400,1000,100]  ,[-2000,-4000,-3000,-5000,-600]]  # 不等式对应参数矩阵
    b = [30000,-20,40000,100000]# 不等式对应的上界
    x1_bd = (0,14)
    x2_bd = (0,8)
    x3_bd = (0,40)
    x4_bd = (0,5)
    x5_bd = (0,50)#各参数的取值范围
    optimize.linprog(c, A_ub=A, b_ub=b, bounds=[x1_bd,x2_bd,x3_bd,x4_bd,x5_bd]) # 调用函数
