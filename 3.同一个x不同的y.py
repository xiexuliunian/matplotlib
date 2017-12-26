#%%
#导包
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

#%%
#设置x,y数据
x = np.linspace(0, 2.0 * np.pi, 101)
y = np.sin(x)
z = np.sinh(x)

xnumber = np.linspace(0, 7, 15)
ynumber1 = np.linspace(-1, 1, 11)
ynumber2 = np.linspace(0, 300, 7)

figure, ax1 = plt.subplots()
ax2 = ax1.twinx()

pic1, = ax1.plot(x, y, color='r', label='sin')
pic2, = ax2.plot(x, z, color='b', label='sinh')
pics=[pic1,pic2]

ax1.legend(pics,[pic.get_label() for pic in pics ])


plt.title('这是一幅图啦')

plt.show()
