l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
l3 = []


string_l1 = ""
string_l2 = ""

#converting data type to string and reversing
for i in reversed(l1):
    string_l1 += str(i)

for i in reversed(l2):
    string_l2 += str(i)

#converting to int and calculating result
result = int(string_l1) + int(string_l2)


# converting back to string for iteration purposes
result_string = str(result)


#reversing and adding result to l3
for i in reversed(result_string):
    l3 += i

print(l1)
print(l2)
print(l3)




