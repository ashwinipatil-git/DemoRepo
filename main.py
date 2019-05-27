

print("Hello World!!")

# Program to display the Fibonacci sequence up to nth term where n is provided by the user

nterms = 7

n1 = 0
n2 = 1
count = 0

if nterms <= 0:
    print("Number should be positive..")
if nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence upto ", nterms, ":")
    while count < nterms:
        print(n1, end=" , ")
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

