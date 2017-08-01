#Printing odd numbers only

for x in range (1,1001):
    if (x % 2 != 0):
        print x

#print multiples of 5

for x in range (5,1000000):
    if (x % 5 == 0):
        print x

#print sum of all values

list = [1,2,5,10,255,3]
sum = 0
for element in list:
    sum += element
print sum

#print average of all values
avg = sum / 2
print avg
