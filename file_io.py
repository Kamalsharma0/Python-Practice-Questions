# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File 1/0
# using Java.
# I like programming in Java.

# WAF that replace all occurrences of "java" with "python" in above file.

f = open("practice.txt", "w")
data = f.write("Hi everyone\nwe are learning File 1/0\nusing Java.\nI like programming in Java.\n")

