from collections import Counter,deque
nums=[1,2,2,3]
c=Counter(nums)
print(c)

dq=deque([1,2,3])
dq.appendleft(0)
print(dq)


import heapq

nums=[4,1,7,3]

heapq.heapify(nums)

print(heapq.heappop(nums))

from itertools import permutations

print(list(permutations([1,2,3,])))

import bisect
arr=[1,2,5,7]
index=bisect.bisect_left(arr,5)
print(index)

arr=[1,2,3]

arr.append(4)
arr.pop()
arr.insert(1,10)
arr.remove(2)
arr.sort()
arr.reverse()

len(arr)
max(arr)
min(arr)

sum(arr)

stack=[]
stack.append(10)
stack.append(20)
print(stack.pop())

s={1,2,3}
s.add(4)
