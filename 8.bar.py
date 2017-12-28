import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('seaborn')
np.random.seed(1212)

range_vals=np.linspace(0,100,11)
print(range_vals)
counts1=np.random.rand(10)*4.0
print(counts1)
counts2=-np.random.rand(10)*8.0
counts3=np.random.rand(10)*2.0
errors=np.ones(10)*1.0
bar_width=5.0

mid_vals=(range_vals[0:-1]+range_vals[1:])*0.5
print(mid_vals)
plt.bar(mid_vals,counts1,facecolor='C3',width=bar_width,label='bar1')
plt.xticks(mid_vals)
plt.legend()
plt.show()