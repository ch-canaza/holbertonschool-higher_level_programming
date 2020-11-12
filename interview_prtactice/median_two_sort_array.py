#!/usr/bin/python3
l1 = [1, 3] 
l2 = [2] 
total = 0
s1 = len(l1)
s2 = len(l2)

new_list = []
i, j = 0, 0

while i < s1 and j < s1:

    if l1[i] < l2[j]:
        new_list.append(l1[i])
        total += l1[i]
        if i+1:
            i += 1

    else:
        new_list.append(l2[j])
        total += l2[j]
        if j+1:
            j += 1
new_list = new_list + l1[i : ] + l2[j : ]
print(total // 2)
print(new_list)



