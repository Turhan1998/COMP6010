data = [0] * 20
print("List with 20 zeroes:\n\t",data)
alternating_bits = [0, 1] * 10
print("List with alternating bits:\n\t",alternating_bits)
rgb = ['r', 'g', 'b'] * 5
print("List with primary colour components:\n\t",rgb)


#Passing lists to a function
def remove_first_item(list):
    print("list in function before modifiying:\n\t",list)
    list.remove(list[0]) # remove first item
    print("list in function after modifiying:\n\t",list)

my_list = ['super', 'nintendo', 'chalmers']
print("actual list before calling function:\n\t",my_list)
remove_first_item(my_list)
print("actual list after function finishes:\n\t",my_list)