import random
import time
from tkinter import *

root = Tk()
root.title("Visualizer")

#draws the lines onto the canvas
def canvasreset(listr):
	for n in range(len(listr)):
		l = c.create_line(4+n*4, height+2, 4+n*4, 400-listr[n], width=divider, fill="white")

#draws red pointer onto the canvas to show current pos of our sort index
def pointer(index, listr):
	l = c.create_line(4+index*4, height+2, 4+index*4, 400-listr, width=divider, fill="red")

height, width = 400, 400

#"width x height"
root.geometry("404x400")

c = Canvas(root, width=width, height=height, bg="black")
global divider
divider = 4
nul = []

for n in range(100):
	nul.append(n*4)

#randomizing algorithm
for n in range(300):
	ran1, ran2 = random.randint(0, len(nul)-1), random.randint(0, len(nul)-1)
	nul[ran1], nul[ran2] = nul[ran2], nul[ran1]

for n in range(len(nul)):
	l = c.create_line(4+n*4, height+2, 4+n*4, 400-nul[n], width=divider, fill="white")
	c.pack()
	root.update()

#bubble sort älgorithm and visualizer
done = 1
while done != 0:
	done = 0
	for i, n in enumerate(nul):
		if i == len(nul)-1:
			break
		else:
			if nul[i] > nul[i+1]:
				nul[i+1], nul[i] = nul[i], nul[i+1]
				c.delete("all")
				canvasreset(nul)
				pointer(i+1, nul[i+1])
				c.pack()
				root.update()
				done += 1
canvasreset(nul)
while True:
	root.update()











"""
																		created by jax0033@protonmail.com
"""