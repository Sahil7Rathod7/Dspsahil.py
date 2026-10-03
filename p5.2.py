@@ -0,0 +1,4 @@
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x,y: x+y, numbers)
print("Sum using reduce:", result)
