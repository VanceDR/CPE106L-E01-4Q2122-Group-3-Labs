"""
Write a program that allows the user to navigate through the lines of text in a file. The program prompts the user for a filename and inputs the lines of text into a list. The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number. Actual line numbers range from 1 to the number of lines in the file. If the input is 0, the program quits. Otherwise, the program prints the line associated with that number.
"""


fileName = input("Enter the file name: ") # File name is LR1/PostLab Q2/num.txt
f = open(fileName, 'r')
lines = []
num_lines = 0
for line in f:
    num_lines += 1
    lines.append(line)
print("Number of lines: ", num_lines)

lineNumber = int(input("Enter a Line Number from 1 to " + str(num_lines) + " to print the line at that line number or 0 to exit: "))
if lineNumber != 0:
    print("The line at",lineNumber,"is:", lines[lineNumber-1])
else:
    print("Program Exited")
