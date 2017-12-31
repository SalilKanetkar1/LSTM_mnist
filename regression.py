from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import random
#style.use('fivethirtyeight')
#xs=np.array([1,2,3,4,5,6],dtype=np.float64)
#ys=np.array([5,4,6,5,6,7],dtype=np.float64)

def create_dataset(hm,variance,step=2,correlation=False):
    val=1
    ys=[]
    for i in range(hm):
        y=val+random.randrange(-variance,variance)
        ys.append(y)
        if correlation and correlation=='pos':
            val=val+step
        elif correlation and correlation=='neg':
            val=val-step
    xs=[i for i in range(len(ys))]
        
    return np.array(xs,dtype=np.float64),np.array(ys,dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):
    m=((mean(xs)*mean(ys)-mean(xs*ys))/
    ((mean(xs)*mean(xs)-mean(xs*xs))))
    
    b=mean(ys)-m*mean(xs)

    return m,b

xs,ys=create_dataset(40,20,2,correlation='pos')
m,b=best_fit_slope_and_intercept(xs,ys)
print(m,b)
regression_line=[(m*x)+b for x in xs]

#sample prediction example
predict_x=8
predict_y=m*predict_x+b

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y)
plt.plot(xs,regression_line)
plt.show()

#calculation of coefficient of detrmination(r_squared)
t=mean(ys)
a1=0
a2=0
for y in ys:
    a1=a1+(y-t)**2
for j in range(len(ys)):
    a2=a2+(ys[j]-m*xs[j]-b)**2

r_squared=1-(a2)/(a1)
print(r_squared)



