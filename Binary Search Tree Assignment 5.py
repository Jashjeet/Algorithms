# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 21:07:21 2019

@author: jashj
"""

class node:
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None
        

class BST:
    def __init__(self):
        self.root=None
        self.s=0
        self.succ=0
        self.pred=0
        self.sum=0
        self.temp=0
        
    
    def insert(self,key):
        
        if self.root==None:
            self.root=node(key)
            
        else:
            new=node(key)
            cur=self.root
        
            while True:
            
                if key<cur.value:
                    if cur.left==None:
                        cur.left=new
                        break
                    else:
                        cur=cur.left
                    
                elif key>cur.value:
                    if cur.right==None:
                        cur.right=new
                        break
                    else:
                        cur=cur.right
                        
    
    
    def contains(self,key):
        if self.root==None:
            return False
        
        elif self.root.value==key:
            return True
        
        cur=self.root
        
        while True:
            if key==cur.value:
                return True
            
            if key<cur.value:
                if cur.left==None:
                    return False
                else:
                    cur=cur.left
                    
            if key>cur.value:
                if cur.right==None:
                    return False
                else:
                    cur=cur.right
                
                
    def inorder(self,cur=None):
        if cur==None:
            if self.root!=None:
                self.inorder(self.root)
        if cur!=None:
            if cur.left!=None:
                self.inorder(cur.left)
            print(cur.value)
            if cur.right!=None:
                self.inorder(cur.right)
                
    




    def size(self,cur=None):
        if cur==None:
            if self.root!=None:
                self.size(self.root)
        if cur!=None:
            if cur.left!=None:
                self.size(cur.left)
            self.s+=1
            if cur.right!=None:
                self.size(cur.right)
                
        return(self.s)



    def smallest(self):
        cur=self.root
        if cur!=None:  
            while True:
                if cur.left!=None:
                    cur=cur.left
                else:
                    return cur.value
        

            
    def largest(self):
        cur=self.root
        if cur!=None:  
            while True:
                if cur.right!=None:
                    cur=cur.right
                else:
                    return cur.value
                
                


    def successor(self,key,cur=None):
        if cur==None:
            self.succ=self.largest()
            if self.root!=None:
                self.successor(key,self.root)
        if self.root!=None:
            if self.succ<=key:
                return ('Value does not exist')
        
        
        if cur!=None:
            if cur.left!=None:
                self.successor(key,cur.left)
                
            if cur.value>key and self.succ>cur.value:
                self.succ=cur.value
                
            if cur.right!=None:
                self.successor(key,cur.right)
                
        return self.succ



    def predecessor(self,key,cur=None):
        if cur==None:
            self.pred=self.smallest()
            if self.root!=None:
                self.predecessor(key,self.root)
        if self.root!=None:        
            if self.pred>=key:
                return ('Value does not exist')
        
        if cur!=None:
            if cur.left!=None:
                self.predecessor(key,cur.left)
                
            if cur.value<key and self.pred<cur.value:
                self.pred=cur.value
                
            if cur.right!=None:
                self.predecessor(key,cur.right)
                
        return self.pred
                
                






    def greaterSumTree(self,cur=None):
        if cur==None:
            if self.root!=None:
                self.greaterSumTree(self.root)
                
                
                
        if cur!=None:
            if cur.right!=None:
                self.greaterSumTree(cur.right)
                
            self.sum=self.sum+self.temp
            self.temp=cur.value
            cur.value=self.sum

                
            if cur.left!=None:
                self.greaterSumTree(cur.left)        



            
            
            
            
            




if __name__=="__main__":
                
                
    
    a=BST()
#    a.insert(4)
#    a.insert(1)
#    a.insert(6)
#    a.insert(0)
#    a.insert(2)
#    a.insert(5)
#    a.insert(7)
#    a.insert(3)
#    a.insert(8)
    a.insert(0)
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    a.insert(7)
    a.insert(8)
    print('Printing inorder')
    a.inorder()
    b=a.contains(8)
    print('contains',b)
    c=a.size()
    print('size',c)
    d=a.smallest()
    print('smallest',d)
    e=a.largest()
    print('largest',e)
    f=a.successor(16)
    print('successor',f)
    g=a.predecessor(3)
    print('predecessor',g)
    print('Printing inorder before GREATERSUMTREE operation')
    a.inorder()
    a.greaterSumTree()
    print('Printing inorder after GREATERSUMTREE operation')
    a.inorder()




        
                