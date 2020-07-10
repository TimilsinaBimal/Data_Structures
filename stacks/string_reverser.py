my_string = input("Enter any string you want to reverse: ")
arr = []
for i in my_string:
    arr.append(i)
reversed_string = ''
while(arr):
    reversed_string+= arr.pop()

print(f"The reversed string is: {reversed_string}")