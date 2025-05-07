start = int(input("Enter the starting value:\n"))
end = int(input("Enter the ending value:\n"))

print("Implementation with a for loop:")
for i in range (start, end+1):
    print(i, end= "  ")
    

print("\nImplementation with a while loop:")
x = start;
while x<=end:
    print(x, end= "  ")
    x+=1
    
