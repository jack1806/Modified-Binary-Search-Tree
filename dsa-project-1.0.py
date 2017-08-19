# Created by jack1806

# DSA project Winter Sem 16-17

#!/usr/bin/python

from flask import Flask
from flask import render_template
# from random import randint


class Node:
    if __name__ == "__main__":
        value = 0
        right = None
        left = None

    def insert(self, item):
        current_node = self
        while True:
            if current_node is None:
                return 1
            elif current_node.value < item.value:
                if current_node.right is None:
                    current_node.right = item
                    return 1
                current_node = current_node.right
            else:
                if current_node.left is None:
                    current_node.left = item
                    return 1
                current_node = current_node.left

    def search(self, val):
        current_node = self
        steps = 0
        nodes_changed = 0
        while True:
            if current_node.value == val:
                steps += 1
                return True, steps, nodes_changed
            if current_node.value < val:
                steps += 1
                if current_node.right is None:
                    steps += 1
                    return False, steps, nodes_changed
                elif current_node.right.value == val:
                    steps += 1
                    return True, steps, nodes_changed
                nodes_changed += 1
                current_node = current_node.right
            else:
                if current_node.left is None:
                    steps += 1
                    return False, steps, nodes_changed
                elif current_node.left.value == val:
                    steps += 1
                    return True, steps, nodes_changed
                nodes_changed += 1
                current_node = current_node.left


class CustomNode:
    if __name__=="__main__":
        value = 0
        right = None
        left = None
        name = None
        right_right = None
        right_left = None
        left_right = None
        left_left = None
    def getChilds(self):
        childs = [self.left_left,self.left,self.left_right,self.right_left,self.right,self.right_right]
        return childs
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
                return True,steps,nodes_changed,current_node
            elif(current_node.value > val):
                steps +=1
                if(current_node.left == None):
                    steps +=1
                    return False,steps,nodes_changed,None
                if(current_node.left.value==val):
                    steps +=1
                    return True,steps,nodes_changed,current_node.left
                elif(current_node.left.value > val):
                    steps +=1
                    if(current_node.left_left == None):
                        steps +=1
                        return False,steps,nodes_changed,None
                    if(current_node.left_left.value==val):
                        steps +=1
                        return True,steps,nodes_changed,current_node.left_left
                    steps+=1
                    nodes_changed+=1
                    current_node = current_node.left_left
                else:
                    if(current_node.left_right == None):
                        steps +=1
                        return False,steps,nodes_changed,None
                    if(current_node.left_right.value==val):
                        steps +=1
                        return True,steps,nodes_changed,current_node.left_right
                    steps+=1
                    nodes_changed+=1
                    current_node = current_node.left_right
            else:
                if(current_node.right == None):
                    steps +=1
                    return False,steps,nodes_changed,None
                if(current_node.right.value==val):
                    steps +=1
                    return True,steps,nodes_changed,current_node.right
                elif(current_node.right.value > val):
                    steps +=1
                    if(current_node.right_left == None):
                        steps +=1
                        return False,steps,nodes_changed,None
                    if(current_node.right_left.value==val):
                        steps +=1
                        return True,steps,nodes_changed,current_node.right_left
                    steps+=1
                    nodes_changed+=1
                    current_node = current_node.right_left
                else:
                    if(current_node.right_right == None):
                        steps +=1
                        return False,steps,nodes_changed,None
                    if(current_node.right_right.value==val):
                        steps +=1
                        return True,steps,nodes_changed,current_node.right_right
                    steps+=1
                    nodes_changed+=1
                    current_node = current_node.right_right


def init():
    n = CustomNode()
    m = Node()
    f = open('adhaar.txt','r')
    l = []
    l2 = {}
    for i in f:
        l.append(int("".join(i.split()[0:3])))
        l2.update({int("".join(i.split()[0:3])):" ".join(i.split()[3::])})
    n.value = int(l[0])
    m.value = n.value
    for i in range(1,len(l)):
        t = CustomNode()
        r = Node()
        t.value = l[i]
        t.name = l2[l[i]]
        r.value = t.value
        n.insert(t)
        m.insert(r)
    return n,m,l2,l


def create_tree(n,m,searchvalue):
    temp = int(searchvalue)
    status,steps,nodes_changed,name = n.search(temp)
    status2,steps2,nodes_changed2 = m.search(temp)
    return status,steps,nodes_changed,name


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<temp>')
def options(temp):
    n,m,l,l2 = init()
    if(temp == 'view'):
        return render_template("view.html",list=l2,dic=l,length=len(l2))
    elif(temp == 'jst'):
        return render_template("jst.html",parent=n.value,childs=n.getChilds())
    return render_template(""+temp+".html")


@app.route('/search/<tosearch>')
def searchfor(tosearch):
    n,m,l, temp = init()
    status, steps, node_ch, node = create_tree(n, m, tosearch)
    return "Steps required : %d<br>Status : %s<br>Nodes Changed : %d<br>Holder name : %s" % (steps, status, node_ch, node.name)


@app.route('/add/<aadhaar>/<name>')
def add(aadhaar,name):
    n,m,l,temp = init()
    status, steps, node, na = create_tree(n, m, int(aadhaar))
    if(status):
        return "Fail , User already Exist"
    s = aadhaar[0:4]+" "+aadhaar[4:8]+" "+aadhaar[8::]+" "
    with open('adhaar.txt','a') as file:
        file.write(s+name+"\n")
        file.close()
    return "Done"


@app.route('/jst/<node>')
def manualnodeview(node):
    n,m,l, temp = init()
    status, steps, node_ch, node = create_tree(n, m, node)
    return render_template("jst.html",parent=node.value,childs=node.getChilds())

if __name__ == '__main__':
    app.run()
    n = CustomNode()
    m = Node()
    n, m, l, temp = init()
