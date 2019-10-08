#Exercise 1
def RecFact(n):
    if n <= 1:
        return 1
    else:
        return n * RecFact(n-1)
print RecFact(5)


#Exercise 2
def RecPower(x,y):
    if x and y >= 0:
        return x*y
    else:
        return 0
print RecPower(2,6)


#Excercise 3
def numOrder(n):
    for x in range(len(n)-1, 0, -1):
        for i in range(x):
            if n[i] > n[i+1]:
                temp = n[i]
                n[i] = n[i+1]
                n[i+1] = temp
    return n

def main():
    lines = []
    print("Enter numbers from 0 to 9 (hit enter twice to bubble-sort): ")
    while True:
        line = raw_input("%3i: " % (len(lines)+1))
        if not line:
            break
        lines.append(line)
    print("Ordered numbers")
    for i, numbers in enumerate(numOrder(lines), 1):
        print("%3i. %s" % (i, numbers))

main()


x = raw_input("press enter to exit")
print x
