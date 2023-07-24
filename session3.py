

### Question -1
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    if num == 3:
        break
    total += num
print(total)    
#Output = 3



### Question -2
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
#Output = 1 3 5



### Question -3
i = 0
while i < 5:
    if i == 3:
        break
    i += 1
print(i)
#Output = 3



### Question - 4
x = 10
y = 5
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")
#Output = x is greater than y



### Question - 5
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')
#Output = 1 2 4 5



### Question - 6
