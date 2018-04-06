# This code created an automated GIF
import imageio
images = []

# Reading in individual images from heatmap_for_gif.py
filenames = []
alpha = 0.4
iterations = [9,19,29,39,49,59,69,79,89,99]

# Create a filename list to store all files names
for i in (iterations):
    filenames.append('map_' + str(alpha) + '_' + str(i) + '.png')

# Create and store GIF in PNG format
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('FINAL_25seconds.gif', images,fps=25)
