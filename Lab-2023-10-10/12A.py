import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path+"\input.txt", "r")
output = open(dir_path+"\output.txt", "w")
for i in f:
    output.write(i.capitalize())
f.close()