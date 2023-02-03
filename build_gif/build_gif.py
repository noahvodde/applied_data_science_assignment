"""Takes a list of images and makes a GIF file from it."""

# Import necessary libraries
import imageio

filenames = ["1.png", "2.png", "3.png", "4.png", "5.png"]
images = list(map(lambda filename: imageio.v2.imread(filename), filenames))
imageio.mimsave("animated_plot.gif", images, fps=55, duration=1.5)
