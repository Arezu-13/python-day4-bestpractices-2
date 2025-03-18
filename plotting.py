import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}) # subplot_kw is a dict. 

# data
x = np.arange(-10, 10, 0.01)
y = np.arange(-10, 10, 0.01)
x, y = np.meshgrid(x, y)
r = np.sqrt(np.pi*x**2+y**2+0j)
z = (np.cos(r))

# surface plot
yta = ax.plot_surface(x,y,z, cmap=cm.gist_ncar)
ax.set_title("Random function")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# remove the grid lines
ax.grid(False)

# remove the ticks
ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_zticks([]) 

# Saving the figure as PNG
plt.savefig(r"C:\Users\arezu\OneDrive\Desktop\MolecularBiophysics\AdvancedScientificPython\Day4\randfunc.png")  

# Showing the plot
plt.show()

# Close the figure after saving to avoid overlap with other plots
plt.close() 


