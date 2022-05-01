#Given a string, e.g., str = 'abcde', output the string 'abcde ' and it reverse 'edcba' using string slicing str[a:b:c].

#str = 'abcde'
#string = str[::-1]
#print(string)



string = "hello"
for c in string[-3::-1]:
    print (c)