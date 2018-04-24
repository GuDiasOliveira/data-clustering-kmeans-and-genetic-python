# encoding: utf-8
import sys
import utils
import matplotlib.pyplot as plt


# Reading the clustered points from input
points = {}
for line in utils.inputs():
	inps = line.split()
	cluster = int(inps[0]) - 1
	if cluster not in points:
		points[cluster] = []
	points[cluster].append((float(inps[1]), float(inps[2])))

# Preparing and plotting points
markers = ['o', '^', 's', '+', '*']
clusters = list(points)
for i in range(len(points)):
	x = [p[0] for p in points[clusters[i]]]
	y = [p[1] for p in points[clusters[i]]]
	plt.plot(x, y, markers[(i / 10) % len(markers)])
plt.show()