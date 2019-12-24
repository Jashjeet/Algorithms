# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:08:15 2019

@author: jashj
"""

import heapq

file = open("pg22799 Project Gutenberg's Peeps at Many Lands.txt", 'r') 

string=file.read()

dict = {}

for i in string:
    if ord(i) >= 32 and ord(i)<= 127:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
idict=dict
heap=[]       
heap = [[freq,[char, '']] for char, freq in dict.items()]
heapq.heapify(heap)

#print('starting heap ', heap)
while len(heap)>1:
#    print('heap ', heap)
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    
    for l in left[1:]:
#        print('left ' , l)
# appending 0 to the left node(smaller)
        l[1] = '0' + l[1]
    for r in right[1:]:
#        print('right ', r)
# appending 1 to the right node(bigger)
        r[1] = '1' + r[1]
# total cost, new node after merger
    heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])


nbits=0
print('Table with codes in sorted order of characters')
a=heap[0][1:]
a.sort()
for i in a:
    print(i)
    nbits+=dict[i[0]]*len(i[1])
print('No. of bits using Huffman coding ',nbits)


bits7=heap[0][0]*7
print('No. of bits using fixed-length encoding using 7 bits per character ',bits7)
    
print('Bits saved ',bits7-nbits)
