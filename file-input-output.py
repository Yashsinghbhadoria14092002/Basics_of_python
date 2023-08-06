s = "Harry is a good boy"
# writing in a file

# using context manager
# with open("test.txt", "w") as f:
#     f.write(s)

# using manually
# fp = open("test.txt", "w")
# fp.write(s)
# fp.close()

# reading in a file

# using context manager
# with open("harry.txt", "r") as f:
#      t = f.read()
#      print(t)

# using manually
fp = open("harry.txt", "r")
t = fp.read()
print(t)