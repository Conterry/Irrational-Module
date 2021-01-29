import irational

k=int(input())
array = []
array[:k] = (0,0) * k
s = (0, 1)
for i in range(0, k):
    array[i] = irational.inp()
    s=irational.add(array[i], s)
print("1/sum = ")
print(irational.prt(irational.div(1, s)))
