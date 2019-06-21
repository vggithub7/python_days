import java.util.*;
import java.io.*;
class Node{
    Node left,right;
    int data;
    Node(int data){
        this.data=data;
        left=right=null;
    }
}
//MY OWN CODE (ONLY SOLUTION CLASS)          ********************************
class Solution{

	public static int getHeight(Node root){
      //Write your code here
      int leftt,rightt;
      if (root==null||(root.left==null && root.right==null))
        return 0;
      else {
        leftt=getHeight(root.left);
        rightt=getHeight(root.right);
        if (leftt>rightt)
            return 1+leftt;
        else 
        return 1+rightt;
      //return (1+Java.lang.Math.max(leftt,rightt));  
      }  
      
    }
//CODE ENDS             ******************************** **********************
    public static Node insert(Node root,int data){
        if(root==null){
            return new Node(data);
        }
        else{
            Node cur;
            if(data<=root.data){
                cur=insert(root.left,data);
                root.left=cur;
            }
            else{
                cur=insert(root.right,data);
                root.right=cur;
            }
            return root;
        }
    }
	 public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int T=sc.nextInt();
        Node root=null;
        while(T-->0){
            int data=sc.nextInt();
            root=insert(root,data);
        }
        int height=getHeight(root);
        System.out.println(height);
    }
}
