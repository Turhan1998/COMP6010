level1_items = []
level2_items = []
level3_items = []



def classify(line):
    counter = 0
    for i in range (len(line)):
        if line[i] == ' ':
            counter +=1
        else:
            break


#opening a txt file and removing spaces
with open("list.txt", "r") as input:
    for line in input:
        if line[-1] == '\n':
            line = line[:-1]
        print(line)
    print("\n")
        
    #now, lets classify them/ define level
    level = classify(line)
    print(level)