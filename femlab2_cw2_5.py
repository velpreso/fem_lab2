#5.1
import numpy as np
import matplotlib.pyplot as plt
x = [1,2,3]
y = [4,6,5]
plt.plot(x,y)
plt.show()

#5.1.1
x = np.arange(0.0, 2.0, 0.01)
y = np.sin(2.0*np.pi*x)
plt.plot(x,y)
plt.show()

#5.1.2
x = np.arange(0.0, 2.0, 0.01)
y = np.sin(2.0*np.pi*x)
plt.plot(x,y,'r:',linewidth=6)
plt.xlabel('Czas')
plt.ylabel('Pozycja')
plt.title('Nasz pierwszy wykres')
plt.grid(True)
plt.show()

#5.1.3
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0.0, 2.0, 0.01)
y1 = np.sin(2.0*np.pi*x)
y2 = np.cos(2.0*np.pi*x)
plt.plot(x,y1,'r:',x,y2,'g')
plt.legend(('dane y1’,’dane y2'))
plt.xlabel('Czas')
plt.ylabel('Pozycja')
plt.title('Wykres')
plt.grid(True)
plt.show()

