phrase = input("Please input your name: ")
print("First character is", phrase[0])
print("Last character is", phrase[-1])

words = phrase.split(" ")

for w in words:
    print(w)