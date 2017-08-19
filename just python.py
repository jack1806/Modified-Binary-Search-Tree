from random import randint
import time
class node:
    if(__name__=="__main__"):
        value = 0
        right = None
        left = None
    def insert(self,item):
        current_node = self
        while(True):
            if(current_node==None):
                current_node = item
                return 1
            elif(current_node.value<item.value):
                if(current_node.right==None):
                    current_node.right = item
                    return 1
                current_node= current_node.right
            else:
                if(current_node.left==None):
                    current_node.left = item
                    return 1
                current_node= current_node.left
    def search(self,val):
        current_node = self
        steps = 0
        nodes_changed = 0
        while(True):
            if(current_node.value == val):
                steps+=1                
                return True,steps,nodes_changed
            if(current_node.value<val):
                steps+=1
                if(current_node.right==None):
                    steps+=1
                    return False,steps,nodes_changed
                elif(current_node.right.value==val):
                    steps+=1
                    return True,steps,nodes_changed
                nodes_changed+=1
                current_node = current_node.right
            else:
                if(current_node.left==None):
                    steps+=1
                    return False,steps,nodes_changed
                elif(current_node.left.value==val):
                    steps+=1
                    return True,steps,nodes_changed
                nodes_changed+=1
                current_node = current_node.left
class custom_node:
    if(__name__=="__main__"):
        value = 0
        right = None
        left = None
        right_right = None
        right_left = None
        left_right = None
        left_left = None
    def insert(self,item):
        item_value = item.value
        current_node = self
        while(True):
            if(current_node.value > item_value ):
                if(current_node.left!=None):
                    if(current_node.left.value>item_value):
                        if(current_node.left_left==None):                        
                            current_node.left_left = item
                            print("Added to LL of :",current_node.value)
                            return 1
                        current_node = current_node.left_left
                    else:
                        if(current_node.left_right==None):
                            current_node.left_right = item
                            print("Added to LR of :",current_node.value)
                            return 1
                        current_node = current_node.left_right;
                else:
                    current_node.left = item
                    print("Added to L of :",current_node.value)
                    return 1
            else:
                if(current_node.right!=None):
                    if(current_node.right.value>item_value):
                        if(current_node.right_left==None):
                            current_node.right_left = item
                            print("Added to RL of :",current_node.value)
                            return 1
                        current_node = current_node.right_left
                    else:
                        if(current_node.right_right==None):
                            current_node.right_right = item
                            print("Added to RR of :",current_node.value)
                            return 1
                        current_node = current_node.right_right
                else:
                    current_node.right = item
                    print("Added to R of :",current_node.value)
                    return 1
    def search(self,val):
        current_node = self
        steps = 0
        nodes_changed = 0
        while(True):
            if(current_node.value == val):
                steps +=1                
                return True,steps,nodes_changed
            elif(current_node.value > val):
                steps +=1
                if(current_node.left == None):
                    steps +=1
                    return False,steps,nodes_changed
                if(current_node.left.value==val):
                    steps +=1
                    return True,steps,nodes_changed
                elif(current_node.left.value > val):
                    steps +=1
                    if(current_node.left_left == None):
                        steps +=1
                        return False,steps,nodes_changed
                    if(current_node.left_left.value==val):
                        steps +=1
                        return True,steps,nodes_changed
                    steps+=1
                    nodes_changed+=1
                    current_node = current_node.left_left
                else:
                    if(current_node.left_right == None):
                        steps +=1                        
                        return False,steps,nodes_changed
                    if(current_node.left_right.value==val):
                        steps +=1
                        return True,steps,nodes_changed
                    steps+=1
                    nodes_changed+=1
                    current_node = current_node.left_right
            else:
                if(current_node.right == None):
                    steps +=1
                    return False,steps,nodes_changed
                if(current_node.right.value==val):
                    steps +=1
                    return True,steps,nodes_changed
                elif(current_node.right.value > val):
                    steps +=1
                    if(current_node.right_left == None):
                        steps +=1
                        return False,steps,nodes_changed
                    if(current_node.right_left.value==val):
                        steps +=1
                        return True,steps,nodes_changed
                    steps+=1
                    nodes_changed+=1
                    current_node = current_node.right_left
                else:
                    if(current_node.right_right == None):
                        steps +=1
                        return False,steps,nodes_changed
                    if(current_node.right_right.value==val):
                        steps +=1
                        return True,steps,nodes_changed
                    steps+=1
                    nodes_changed+=1
                    current_node = current_node.right_right
n = custom_node()
m = node()
l = [i for i in range(int(input("Number of inputs: ")))]
n.value = len(l)//2
m.value = n.value

for i in l:
	t = custom_node()
	r = node()
	t.value = i
	r.value = i
	n.insert(t)
	m.insert(r)
'''for i in range(len(l)):
    t = custom_node()
    r = node()
    j = randint(0,len(l)-1)
    t.value = l[j]
    r.value = t.value
    del l[j]
    n.insert(t)
    m.insert(r)'''
while(True):
	temp = int(input("Enter elment to search :"))
	init = time.time()
	status,steps,nodes_changed = n.search(temp)
	print("Status JST :",status)
	print("Steps JST :",steps)
	print("Nodes Changed JST :",nodes_changed)
	final = time.time()
	print("Difference :",final-init)
	init = time.time()
	status2,steps2,nodes_changed2 = m.search(temp)
	print("Status BST :",status2)
	print("Steps BST :",steps2)
	print("Nodes Changed BST :",nodes_changed2)
	final = time.time()
	print("Difference :",final-init)
