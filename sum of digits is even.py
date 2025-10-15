list1 = [1,2,3,55,99,108,22]
list2 = [22,32,42,55,65,77]
value = 0
for num in list1 + list2:
    prev=value
    value+=num
    if value % 2 == 0:
       print(f"{prev} + {num} = {value} ,even number")
    else:
        print(f"{prev} + {num} = {value} , odd number")
