# to find square root of a number
n=int(input("Enter the value of n: "))
x=n/2.0
while True:
    root=(x+n/x)/2.0
    if abs(x-root)<0.00001:
        print("Square root of", n, "=", root)
        break
    x=root

# thanks for watching
# like ,share & subscribe to
# Dream2code
