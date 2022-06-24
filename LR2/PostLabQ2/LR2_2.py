filename = input("Enter the File Name:")
f = open("PostLabQ2/numbers.txt", 'r')

count = 0
for line in f:
    count = count + 1
print("The file has "+str(count)+" lines.");
f.close()
while True:
    try:
        n = int(input("Enter a line number [0 to quit]: "))
        lineno = 0
        break;
    except ValueError:
        print("Try again. Line number must be between 0 and "+str(count))
while n != 0:
    
    if n >= 0 and n <= count:
        f = open("PostLabQ2/numbers.txt", 'r')
        for line in f:
            lineno = lineno + 1
            if lineno == n:
                print(line)
        f.close()
    else:
        print("Try again. Line number must be between 0 and "+str(count))
    while True:
        try:
            n = int(input("Enter a line number [0 to quit]: "))
            lineno = 0
            break;
        except ValueError:
            print("Try again. Line number must be between 0 and "+str(count))