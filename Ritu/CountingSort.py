import numpy as np
input=[2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
maxV=max(input)
minV=min(input)
range=(maxV-minV)+1

output=np.zeros(len(input))

print(range)

count=np.zeros(range)
print(input)

for i in xrange(len(input)):
    num=input[i]
    count[num]=count[num]+1

print(count)

start=0
last=0


print("*************************")
for i in xrange(len(count)):
    last=int(start+count[i]-1)
    output[start:last+1]=i
    print(output)
    start=last+1
print(output)

