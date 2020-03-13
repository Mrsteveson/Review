import math
​
class Circle:
	def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r
​
class Sector:
	def __init__(self, contents, orientation, split_coord):
		self.contents = contents
		self.orientation = orientation
		self.split_coord = split_coord
		# index 0 = left/top
		# index 1 = right/bottom
		self.children = None
​
​
root = Sector(None, "vertical", 500)
​
left1 = Sector(None, "horizontal", 200)
right1 = Sector(None, "horizontal", 220)
​
# From the left1
top1 = Sector([Circle(100,80,20), Circle(300,90,20), Circle(240,190,20), Circle(450,170,20)], None, None)
bottom1 = Sector([Circle(250,300,20), Circle(400,220,20), Circle(390,350,20)], None, None)
​
# From the right1
top2 = Sector([Circle(550,200,20), Circle(560,110,20), Circle(650,190,20), Circle(750,100,80)], None, None)
bottom2 = Sector([Circle(530,300,20), Circle(650,290,20), Circle(800,230,20)], None, None)
​
root.children = [left1, right1]
left1.children = [top1, bottom1]
right1.children = [top2, bottom2]
​
def find_circle(root, x, y):
	# Follow the tree to a leaf node
	current = root
​
	while current.children is not None:
		if current.orientation == "vertical":
			current_coord = x
		else:
			current_coord = y
​
		if current_coord < current.split_coord:
			# go left/up
			current = current.children[0]
		else:
			# go right/down
			current = current.children[1]
​
​
	# Search the contents of the leaf node for a collision
​
	for c in current.contents:
		# See if the x,y point is in the circle
		dx = x - c.x
		dy = y - c.y
​
		#dist = math.sqrt(dx*dx + dy*dy)
		dist2 = dx*dx + dy*dy
​
		if dist2 <= c.r*c.r:
			return c
​
	return None
​
print(find_circle(root, 0, 0))
print(find_circle(root, 550, 220))
