#Exercise 2
numbers = [454, 453, 457]
print max(numbers)

#Exercise 3
x = "I enjoy nature"
y = "I enjoy reading"

def longStr(x,y):
    if len(x) > len(y):
        return x
    return y
print longStr(x, y)


#Exercise 4
def rev(sentence):
    x = ""
    for y in sentence:
     x = y + x
    return x
print rev("you are as loud as silence")

print("\n")

#Exercise 1
while True:
    def rps():
            player = raw_input("Select Paper, Rock or Scissors: ")

            if player == "scissors" or player == "s":
                return "Computer plays Paper. You win!"
                
            if player == "rock" or player == "r":
                return "Computer plays Scissors. You win!"
                
            if player == "paper" or player == "p":
                return "Computer plays Rock. You win!"

    print rps()
