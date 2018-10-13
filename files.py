file = open("myfile.txt","w")
file.write("hello")
file.close()

try:
    file = open("myfile2.txt","r")
    contents = file.read()
    print(contents)
    file.close()
except:
    print("You failed. I'm going to do the work for you.")
    file = open("myfile2.txt","w")
    file.close()
