"""
Statisticians would like to have a set of functions to compute the median and mode of a list of numbers. The median is the number that would appear at the midpoint of a list if it were sorted. The mode is the number that appears most frequently in the list. Define these functions in a module named stats.py. Also include a function named mean, which computes the average of a set of numbers. Each function expects a list of numbers as an argument and returns a single number.
"""
from mean import compute_mean
from mode import compute_mode
from median import compute_median

def main():
    numbers = []

    input_type = int(input("Enter Input Type: 1 (Text File Input), 2 (Command Line Input): "))
    if input_type == 1:
        fileName = input("Enter the file name: ") # File name is LR1/PostLab Q1/num.txt
        f = open(fileName, 'r')
        for line in f:
            words = line.split()
            for word in words:
                numbers.append(float(word))
    else:
        num = int(input("Enter a Number to Add to the List (999 to Stop): "))
        while num != 999:
            numbers.append(num)
            num = int(input("Enter a Number to Add to the List (999 to Stop): "))

    print("The created list of numbers is: ",numbers)
    select = int(input("Select Function 0 (Median), 1 (Mode), 2 (Mean): "))
    if select == 0:
        print("The median is ",compute_median(numbers))
    if select == 1:
        print("The mode is ",compute_mode(numbers))
    if select == 2:
        print("The mean is ", compute_mean(numbers))    

if __name__ == "__main__":
    main()
