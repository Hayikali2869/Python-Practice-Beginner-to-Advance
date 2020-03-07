import random
import math

x = random.uniform(0,2)
print(x)

# Random int such that a<x<b
print(random.randint(2,10))
# Returns a random element from the non-empty
# sequence seq.

print(random.choice('asdasdaxxx'))
# Returns the next random floating point number in the
# range 0.0, 1.0
random.random()

# Shuffle the sequence x in place.
list = ['123', '234', '345']
lst = [111, 222, 333]
random.shuffle(list)
random.shuffle(lst)
# No idea why there's a space before lst
print(list, '\n', lst)

# \n use to change a new line
print('ahahahah\nelloworld')


print()
print(math.ceil(1000.1))
print(math.floor(3.14))
print(math.sqrt(3.14))
print(math.cos(45))
print(math.sin(45))
print(math.tan(90))

# Converts angle x from radians to degrees.
print(math.degrees(1))
# Converts angle x from degrees to radians.
print(math.radians(1))
# Print(math.radians(1))
print(math.pi)