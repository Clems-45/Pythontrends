f = open("workfile.txt", "w+")

f.write("This is a test\n ")
f.read()

file = open("testfile.txt", "w")

file.write("Hello World")
file.write("This is our new text file")
file.write("and this is another line.")
file.write("Why? Because we can.")

file.close()
