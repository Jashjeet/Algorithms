# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:26:00 2019

@author: jashj
"""




if __name__=='__main__':
    
    solution=[]# contains the list of combinations
    count=0# initializing the counter at 0
        
    n=int(input('Enter n: '))
    
    
    k=int(input('Enter k: '))
    
    if 1<=k and k<=10:
        c=[[i] for i in list(map(int, input('Enter distinct '+str(k)+' numbers between 1 and 10, in ascending order, separated by a space: ').split()))]
        
        if k==len(c):
            for i in c:
                if sum(i)==n and i not in solution:
                    count+=1 #keeping count of number of set which add up to n. these are base cases also.
                    solution.append(i)
                for j in c:
                    if sum(i)+sum(j)<=n and i+j not in c:# memoization. d is a list storing distinct values.
                        c.append(i+j)
                        if sum(i)+sum(j)==n:
                            count+=1 #keeping count of number of set which add up to n
                            solution.append(i+j)
                            
            print('The number of combinations is: ',count)
            print('Partitions:')
            for i in solution:
                print(i)
        else:
            print('Exactly ',k,' numbers should be entered. Please run the program again.')
        
    else:
        print('k should lie between 1 and 10')
        exit()
