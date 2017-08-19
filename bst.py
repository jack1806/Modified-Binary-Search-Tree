from random import randint
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
n = node()
n.value = int(input("Parent Value: "))
print(n.value,n.left,n.right)
l = [i for i in range(int(input("Number of inputs: ")))]
for i in range(len(l)):
    t = node()
    j = randint(0,len(l)-1)
    t.value = l[j]
    del l[j]
    n.insert(t)
status,steps,nodes_changed = n.search(int(input("Enter elment to search :")))
print("Status :",status)
print("Steps :",steps)
print("Nodes Changed :",nodes_changed)