FibCount = int(input("How many numbers in the Fibonacci Sequence would you like to generate?\n"))-3
Lasta = 1
Lastb = 2
print("0")
print("1")
print(Lasta)
print(Lastb)
morestate = "true"
while morestate == "true":
    for x in range(1, FibCount):
        Num = Lasta+Lastb
        print(Num)
        Lasta = Lastb
        Lastb = Num
    more = input("Would you like to generate more numbers in the Fibonacci Sequence? y/n\n")
    if more == "y":
        FibCount = int(input("How many more numbers would you like to generate?\n"))+1
        morestate = "true"
    if more == "n":
        morestate = "false"
    

    
    
    
