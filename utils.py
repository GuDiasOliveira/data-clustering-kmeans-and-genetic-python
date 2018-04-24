# encoding: utf-8
import sys


def readinput():
	try:
		line = raw_input().strip()
		while line == '' or line.startswith('#'):
			line = raw_input().strip()
		return line
	except EOFError:
		return None

def inputpoints():
	points = []
	inp = readinput()
	while inp != None:
		inputs = inp.split()
		p = float(inputs[0]), float(inputs[1])
		points.append(p)
		inp = readinput()
	return points

def inputs():
	line = readinput()
	while line != None:
		yield line
		line = readinput()