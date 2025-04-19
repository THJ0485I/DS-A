mydata2 = "13 34 2 10 6 18"
# split the mydata2 into list2
# convert all the items in the list2 into int datatype
list2 = mydata2.split()
# sum the qnd and 3rd largest highest value
list3 = []
list4 = []
for i in range(len(list2)):
  list3.append(int(list2[i]))

for v in list2:
    list4.append(int(v))

list5 = [int(x) for x in list2]

print(list2)
print(list3)
print(list4)

######################################

n = int(input())
gift = [0]
data = input().split()

for v in data:
    gift.appennd(int(v))
print(gift)
student = [0] * (n + 1)

for si in range(n+1):
    for gi in range(n+1):
        if gift[gi] == si: 
            student[si] = gi

print(student)

#########################

lengths = [int(x) for x in input().split()]
print(length)

############################################

listA = [2, 3, 5, 7, 11, 13, 17]
print(listA)

for listA in range (int(len(listA))):
    print(listA, end="")
print()

listA.append(input("Enter a prime number: "))
print(int(listA))

#################################### 

#sorting
listb = ["Wallace", "Ishan", "Jayrius", "Sofie", "jayrius", "Ishaan"]
listb.sort(reverse = True)
print(listb)

###################################3
# list
lista = ["24", "17", "14", "12", "29"]

# 2nd largest and 2nd smallest
lista.sort()
temp = lista[0]
for num in lista:
    if num != temp:
        print(num)
        break

lista.sort(reverse=True)
temp = lista[0]
for num in lista:
    if num != temp:
        print(num)
        break

# average of all even numbers
total = 0
numofeven = 0
for num in lista:
    if num % 2 == 0:
        total += num
        numofeven += 1

lista.sort()
print(lista)

#################################

# Exercise 1






