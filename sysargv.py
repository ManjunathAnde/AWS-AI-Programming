import sys
filename = sys.argv[1] #first arguement is always script name

'''prints and opens the contents of the first filename we enter in terminal '''
with open(filename, "r") as f:
    print(f.read()) 
