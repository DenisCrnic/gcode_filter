# Function to convert list to string
def listToString(line_list):  
    line_str = ""  # initialize an empty string 
    for word in line_list: # Iterrate through the list   
        line_str += word + " " # Append single words wirh spaces to string line

    return line_str # Return final line_str  

# Function which writes a line to file, if input line is list instead
# of string it converts it to string. Function appends a new line character
# to the end of each line
def writeLine(f, line):
    if type(line) == list:
        f.write(listToString(line) + "\n")
    elif type(line) == str:
        f.write(line + "\n")

with open('input.nc') as f: # Opens file as variable f
    file_str = f.read() # Read string from f to file_str
    # print(file_str)
f.close() # Close input file

file_str_sliced = file_str.split("\n") # Slice lines into list

# print(file_str_sliced)

letter = input("Input letter: ") # Input selected letter which you want to change
number = input("Input number: ") # Input new values for selected letter

f = open("output.nc", "w") # Open output file

occurences = 0
import time
start_time = time.time()

for i in range(0, len(file_str_sliced)): # Iterrate through list of lines
    line = file_str_sliced[i] # Read line into line string
    print(str(i + 1) + ". " + line) # Print every input line so we can see how program is progressing

    if "C" in line and letter in line: # If line contains C and selected letter
        occurences += 1
        print("------------------------------")
        print("Found a match on line {}".format(i + 1))
        line_sliced = line.split(" ") # Split line by " " to obtain words in line_sliced
        print(line_sliced)
        # Iterrate through words of single line to find which word should get modified
        for i in range(0, len(line_sliced)):
            word = line_sliced[i]
            if letter in word: # Find the word containing selected letter
                line_sliced[i] = letter + number # Modifiy value of line
        print("Modified it to \n {}".format(line_sliced))
        writeLine(f, line_sliced) # Write line to new file
        print("------------------------------")

    else: # Just write last line to file without modification
        writeLine(f, line)
    
f.close() # Close final output.nc file
print("Found {} occurences in {} s".format(occurences, int(time.time() - start_time)))