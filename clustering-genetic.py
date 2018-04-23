# encoding: utf-8
import sys
from random import shuffle
from random import randint
from math import sqrt
import io


# Reading input and validating
clustersCount = int(sys.argv[1])
if clustersCount <= 0:
	print >> sys.stderr, 'Invalid input: The number of clusters must be positive and non-zero!'
	exit(1)
data = io.input()
popSize = 30
numIterations = 150

# Generating initial population
pop = []
for i in range(popSize):
	ind = [x % clustersCount for x in range(len(data))]
	shuffle(ind)
	pop.append(ind)

def distance(x1, x2):
	dx = x2[0] - x1[0]
	dy = x2[1] - x1[1]
	return sqrt(dx * dx + dy * dy)

def fitness(ind):
	f = 0
	for i in range(len(ind)):
		for j in range(i):
			dist = distance(data[i], data[j])
			f += dist if i != j else -dist
	return f

for k in range(numIterations):
	nextGen = []
	for i in range(len(pop) / 2):
		# Selecting 4 distinct individuals
		parentIds = set()
		while len(parentIds) < 4:
			parentIds.add(randint(0, len(pop) - 1))
		parentIds = list(parentIds)
		# Selecting 2 parents with binary tournament
		parent1 = pop[parentIds[0]] if fitness(pop[parentIds[0]]) > fitness(pop[parentIds[1]]) else pop[parentIds[1]]
		parent2 = pop[parentIds[2]] if fitness(pop[parentIds[2]]) > fitness(pop[parentIds[3]]) else pop[parentIds[3]]
		# Doing crossover
		cutPoint = len(data) / 2
		child1 = parent1[:cutPoint] + parent2[cutPoint:]
		child2 = parent2[:cutPoint] + parent1[cutPoint:]
		# Doing mutation
		if randint(1, 30) == 1:
			idx = randint(0, len(data) - 1)
			child1[idx] = randint(0, clustersCount - 1)
		if randint(1, 30) == 1:
			idx = randint(0, len(data) - 1)
			child2[idx] = randint(0, clustersCount - 1)
		# Adding children to the new generation population
		nextGen.append(child1)
		nextGen.append(child2)
	pop = nextGen

# Selecting the best solution, the final one
sol = pop[0]
bestf = fitness(sol)
for i in range(1, len(pop)):
	f = fitness(pop[i])
	if f > bestf:
		bestf = f
		sol = pop[i]

# Printing output solution
print '#\tCluster\t\tX\t\tY'
for i in range(len(data)):
	print ' \t%d\t\t%f\t\t%f' % (sol[i] + 1, data[i][0], data[i][1])