@@ -0,0 +1,26 @@
#Tuple operations
t = (10,20,30,40)
print("Tuple element:", t[1])

#Set operations
S={1,2,3,4}
S.add(5)
S.remove(2)
print("Set:", S)

#Dictionary operations
student = {"name":"Amit","age":20,"marks": 85}

print("Name:", student["name"])

student["marks"] = 90

student["city"] = "Nagpur"

del student["age"]

print("Updated Dictionary:",student)

print("Dictionary keys:", student.keys())
print("Dictionary values:", student.values())
print("Dictionary items:", student.items())
