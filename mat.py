>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> x=np.linspace(0,10,20)
>>> y=x**2
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000001F751F74FC8>]
>>> plt.show()
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000001F750180588>]
>>> plt.title("plot1")
Text(0.5, 1.0, 'plot1')
>>> plt.xlabel('x')
Text(0.5, 0, 'x')
>>> plt.ylabel('y')
Text(0, 0.5, 'y')
>>> plt.show()