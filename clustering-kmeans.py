# encoding: utf-8
import sys
import io
from math import sqrt
from random import randint


# Reading input and validating
clustersCount = int(sys.argv[1])
if clustersCount <= 0:
	print >> sys.stderr, 'Invalid input: The number of clusters must be positive and non-zero!'
	exit(1)
data = io.input()
precision = 1e-6

# Calculating initial centers
randIndexes = set()
while len(randIndexes) < clustersCount:
	randIndexes |= {randint(0, len(data) - 1)}
centers = [data[i] for i in randIndexes]
del randIndexes

def distance(p1, p2):
	dx = p2[0] - p1[0]
	dy = p2[1] - p1[1]
	return sqrt(dx * dx + dy * dy)

# Running k-means to cluster data
clusters = None
centerDiff = float('inf')
while centerDiff >= precision:
	clusters = []
	# Classifying by nearest centers
	for p in data:
		minCenterDist = float('inf')
		nearestCenterIndex = None
		for i in range(len(centers)):
			dist = distance(p, centers[i])
			if dist < minCenterDist:
				minCenterDist = dist
				nearestCenterIndex = i
		clusters.append(nearestCenterIndex)
	# Calculating new centers
	newCenters = []
	for i in range(clustersCount):
		avgX = 0.0
		avgY = 0.0
		countX = 0
		countY = 0
		for j in range(len(data)):
			if clusters[j] == i:
				avgX += data[i][0]
				avgY += data[i][1]
				countX += 1
				countY += 1
		avgX /= countX
		avgY /= countY
		newCenters.append((avgX, avgY))
	# Calculating centers dislocation
	maxCenterDiff = 0.0
	for i in range(len(centers)):
		diff = distance(centers[i], newCenters[i])
		if diff > maxCenterDiff:
			maxCenterDiff = diff
	centerDiff = maxCenterDiff
	centers = newCenters

# Printing output solution
print '#\tCluster\t\tX\t\tY'
for i in range(len(data)):
	print ' \t%d\t\t%f\t\t%f' % (clusters[i] + 1, data[i][0], data[i][1])