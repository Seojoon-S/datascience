'''
import random
List = []
for _ in range(10) :
    List.append(random.randint(1,10))
print(List)
print(List.count(7))
List.sort()
print(List)
List.reverse()
print(List)
'''
List = []
while True :
    n = int(input())
    if n < 0 :
        break
    List.append(n)
List.sort()
print(List)
