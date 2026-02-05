# Create a NamedTuple in Python

from collections import namedtuple

# Define a namedtuple
Vertex = namedtuple("Vertex", ["x", "y"])

# Create an instance
v = Vertex(10, 20)

# Access fields
print("Vertex-1:", v.x)
print("Vertex-2:", v.y)

# Access NamedTuple Fields

# Example: Accessing by Indexing

from collections import namedtuple

# Define a namedtuple
Point = namedtuple("Point", ["x", "y"])

# Create an instance
p = Point(10, 20)

# Access fields by indexing
print("Point-1", p[0])
print("Point-2", p[1])

# Example Accessing by keyname

from collections import namedtuple

# Define a namedtuple
Point = namedtuple("Point", ["x", "y"])

# Create an instance
p = Point(10, 20)

# Access fields by keyname
print("Point-1:", p.x)
print("Point-2:", p.y)

# Example: Accessing Using getattr()

from collections import namedtuple

# Define a namedtuple
Point = namedtuple("Point", ["x", "y"])

# Create an instance
p = Point(10, 20)

# Access fields using getattr()
print("getattr(p, 'x'):", getattr(p, "x"))
print("getattr(p, 'y'):", getattr(p, "y"))


# The _replace() method


from collections import namedtuple

# Define a namedtuple
Point = namedtuple("Point", ["x", "y"])

# Create an instance
p = Point(10, 20)

# Replace a field value
p2 = p._replace(x=30)

# Access fields
print("p2.x:", p2.x)
print("p2.y:", p2.y)


# The _make() method

from collections import namedtuple

# Define a namedtuple
Point = namedtuple("Point", ["x", "y"])

# Create an instance
p = Point(10, 20)

# Create a new instance using _make()
p2 = Point._make([30, 40])

# Access fields
print("p2.x:", p2.x)
print("p2.y:", p2.y)
