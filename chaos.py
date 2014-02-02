import math
import random
import matplotlib.pyplot as plt
import sys

class ChaosGame:
	def __init__(self, initial_point, ratio = 0.5, number_of_points = 3):
		self.initial_point = initial_point
		self.ratio = ratio
		self.number_of_points = number_of_points
		if self.number_of_points == 3:
			self.points = [(0.0, 0.0), (1.0, 0.0), (0.5, math.sqrt(1 - 0.5 ** 2))]

	def generate_sequence(self, iterations):
		self.sequence = []
		for x in range(iterations):
			self.sequence.append(random.randint(0, self.number_of_points - 1))

	def generate_points(self, iterations):
		self.generate_sequence(iterations)
		self.gen_points = []
		for x in range(iterations):
			if x == 0:
				point_x = (self.initial_point[0] * (1 - self.ratio)) + ((self.points[self.sequence[x]][0]) * self.ratio)
				point_y = (self.initial_point[1] * (1 - self.ratio)) + ((self.points[self.sequence[x]][1]) * self.ratio)
				self.gen_points.append((point_x, point_y))
			else:
				point_x = (self.gen_points[x - 1][0] * (1 - self.ratio)) + ((self.points[self.sequence[x]][0]) * self.ratio)
				point_y = (self.gen_points[x - 1][1] * (1 - self.ratio)) + ((self.points[self.sequence[x]][1]) * self.ratio)
				self.gen_points.append((point_x, point_y))

	def print_points(self):
		for x in self.gen_points:
			print(str(x[0]) + " | " + str(x[1]))

	def plot_points(self):
		for x in self.gen_points:
			plt.plot([x[0]], [x[1]], 'ro')
		plt.axis([0, 1, 0, 1])
		plt.show()

if len(sys.argv) < 4:
	print "Usage : python chaos.py [initial point ordinate] [initial point abcissa] [number of iterations] [value of r]"
else:
	init_point = (float(sys.argv[1]), float(sys.argv[2]))
	if len(sys.argv) == 4:
		c = ChaosGame(init_point)
	else:
		c = ChaosGame(init_point, float(sys.argv[4]))
	
	c.generate_points(int(sys.argv[3]))
	c.plot_points()
