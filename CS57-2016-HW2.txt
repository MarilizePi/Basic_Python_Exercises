#Excercise 1
#A
sum = 0
for x in range(0,101):
    if(x%2)== 0:
        sum+=x
print "The sum of even numbers from 0 to 100 is: ", sum

x = 100
while x >= 0:
    print x, sum
    x -= 2

    
print("\n")
#B
sum = 0
for x in range(0,100):
    if(x%2)!= 0:
        sum+=x
print "The sum of odd numbers from 0 to 100 is: ", sum

x = 101
while x >= 0:
    print x, sum
    x -= 2


print("\n")
#Excercise 2
print "To be or not to be: that's the question!"
sentence = "To be or not to be: that's the question!"
vowels = "aeiou"
for v in vowels:
    print v, sentence.lower().count(v)


print("\n")
#Excercise 3
C = int(raw_input("Type a temperature in Censius in order to convert it into Fahrenheit: "))
F = C * 1.8 + 32
print F


print("\n")
#Exercise 4
#A
print "sum from 1 to 20"
sum = 0
for x in range(1,20):
      sum += x
print(sum)


print ("\n")
#B
x = int(raw_input("Enter any number: "))
sum = 0
for x in range(1,x):
      sum += x
print(sum)


print ("\n")
x = input("press enter to exit")
print x
