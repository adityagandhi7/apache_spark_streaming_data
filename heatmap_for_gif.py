# The code creates a heatmap for 10 iterations at alpha= 0.4. 
# Running this code successively we create heatmap images that are used to create a GIF in automated_gif.py
import numpy as np
import numpy.random
import matplotlib.pyplot as plt

# Initialization of values
iter_0_val = []
alpha = 0.4

# Iterate through all input files,starting at the 9th iteration
iterations = [9]

# Read files and convert to float for heatmap
for i in iterations:
    with open('output_gif_0.4_' + str(i) + '.txt', 'r') as f:
        for y in f.readlines():
            iter_0_val.append(float(y))

# Restructuring the data in the 1000 x 1000 form
iter_0_val_rs = np.reshape(iter_0_val, (1000, 1000))

# Create individual heatmap image
plt.imshow(iter_0_val_rs, cmap='hot', interpolation='nearest', aspect='auto')
ax = plt.gca()
ax.invert_yaxis()

# Save heatmap created
plt.savefig('map_' + str(alpha) + '_' + str(i) + '.png', dpi=100)
