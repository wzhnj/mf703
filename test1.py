import random
print(random.randint(1,2))
data=[]
data1=[]
for i in range(10000):
    data.append(random.randint(1,2))
print(data)
for i in range(10000):
    data1.append(data[i])
    if(data[i]==2):
        data1.append(1)
    else:
        data1.append(2)
print(data1)
sum1=0
sum2=0
for i in range(20000):
    if (i%2==0):
        sum1=sum1+data1[i]
    else:
        sum2=sum2+data1[i]
print(sum1,sum2)
    