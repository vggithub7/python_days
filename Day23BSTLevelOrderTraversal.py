import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
  	     #Write your code here
        tracversal = ''
        if root!=None:
            queue=[root]
            while(len(queue)!=0):
                print queue[0].data,
                #tracversal=tracversal+str(queue[0].data)+ " "
                if queue[0].left!=None:
                    queue.append(queue[0].left)
                if queue[0].right!=None:
                    queue.append(queue[0].right)
                queue.pop(0)
            
        #print(tracversal)
T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
