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
## MY CODE STARTS HERE(GET HEIGHT FUNCTION#)######################################
    def getHeight(self,root):
        #Write your code here
        leftt=right=0
        if (root==None or (root.left==None and root.right==None)):
            return 0
        else:
            leftt=self.getHeight(root.left)
            rightt=self.getHeight(root.right)
            return 1+max(leftt,rightt)
### MY CODE ENDS HERE                    #############################################            
T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height      
