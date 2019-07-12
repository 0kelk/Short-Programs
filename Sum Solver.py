thesum = input("Input a sum\n")
sumelements = []
for x in range(len(thesum)):
    sumelements.append(thesum[x])
for x in range(len(sumelements)):
    int(sumelements[x])
if sumelements[1] == "+":
    print(sumelements[0]+sumelements[2])
if sumelements[1] == "-":
    print(sumelements[0]-sumelements[2])
if sumelements[1] == "x" or sumelements[1] == '*':
    print(sumelements[0]*sumelements[2])
if sumelements[1] == "/":
    print(sumelements[0]/sumelements[2])    
    
    
