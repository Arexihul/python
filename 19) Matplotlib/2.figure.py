import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x**3
z = x**2

"""
# *** Örnek 1 ***

figure = plt.figure()

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])

axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("x Axis")
axes_cube.set_ylabel("y Axis")
axes_cube.set_title("Cube")

axes_square = figure.add_axes([0.15,0.6,0.25,0.25])

axes_square.plot(x,z,"r")
axes_square.set_xlabel("x Axis")
axes_square.set_ylabel("y Axis")
axes_square.set_title("Square")
"""

"""
# *** Örnek 2 ***

figure = plt.figure()

axes = figure.add_axes([0,0,1,1])

axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")

axes.legend(loc=4)      # loc could be 1,2,3,4  1 => Sağ üst köşe  2 => Sol üst köşe(varsayılan)  3 => Sol alt köşe  4 => Sağ alt köşe
"""


# *** Örnek 3 ***

fig,(axes1,axes2) = plt.subplots(nrows=2,ncols=1,figsize=(6,6))

axes1.plot(x,y)
axes1.set_title("Cube")

axes2.plot(x,z)
axes2.set_title("Square")

plt.tight_layout()

fig.savefig("figure1.pdf")

plt.show()
