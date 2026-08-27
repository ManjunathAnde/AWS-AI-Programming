import sys
filename = sys.argv[1] #first arguement is always script name

'''prints and opens the contents of the first filename we enter in terminal with error handling '''
try:
    with open(filename, "r") as f:
        print(f.read())

except IndexError:
    print("Please provide a filename")
except FileNotFoundError:
    print("There is no such file in the project folder")

try:
    with open(filename,"a") as f:
        f.write("This line has been written through a script\n")
except FileNotFoundError:
    print("There is no such file in the folder")
    