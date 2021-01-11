f = open("files.example", "r")
s = f.read()
f.close()

f = open("files.example", "w")
f.write("All is going to be ok \n")
#^Overwrites whatever is in the file
f.write('Everything is under control')
#^Adds to the already existing overwrite
f.close()

f = open("files.example", "r")
lines = f.readlines()
f.close()

f = open("files.example", "r")
line1 = f.readline(1)
line2 = f.readline(2)

