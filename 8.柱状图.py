#导包
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('seaborn')#设置绘图风格
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

np.random.seed(1212)#设定一个random种子

range_vals=np.linspace(0,100,11)    #[   0.   10.   20.   30.   40.   50.   60.   70.   80.   90.  100.]
counts1=np.random.rand(10)*4.0      #[ 0.98114884  3.21700231  0.69793649  3.87808528  0.90194182  3.4768705 1.12586383  2.9016785   3.00952051  0.98668451]
counts2=np.random.rand(10)*8.0      #[ 6.17411605  0.68543392  7.1312601   1.74432108  7.47576203  0.72468599 6.45815633  3.11734471  7.55195589  0.13507939]
counts3=np.random.rand(10)*2.0      #类似的
errors=np.ones(10)*0.2
bar_width=2.0                       #设置bar的宽度

mid_vals=(range_vals[0:-1]+range_vals[1:])*0.5  #[  5.  15.  25.  35.  45.  55.  65.  75.  85.  95.]
groups=['甲','乙','丙','丁','戊','戌','庚','辛','任','癸']
# print(mid_vals)
plt.bar(mid_vals,counts1,facecolor='C3',width=bar_width,label='bar1',yerr=errors)
plt.bar(mid_vals+2,counts2,color='C4',width=bar_width,label='bar2')
plt.bar(mid_vals+4,counts3,color='C5',width=bar_width,label='bar3')
# plt.xticks(mid_vals)
plt.xticks(mid_vals,groups,rotation='horizontal')#将值给grops代替
plt.legend()
# plt.grid()
plt.show()