
import java.util.*;

import javax.sound.midi.SysexMessage;

public class Tree {
    public static void main(String args[])
    {
        Trees t =new Trees();
        t.insert(7);
        t.insert(4);
        t.insert(9);
        t.insert(1);
        t.insert(6);
        t.insert(8);
        t.insert(10);

        System.out.println(t.find(t.root, 90));
        System.out.print("preorder\n");
        t.preorder(t.root);
        System.out.print("postorder\n");
        t.postorder(t.root);
        System.out.println("inorder\n");
        t.inorder(t.root);
        System.out.println("\n");
        System.out.println("height:");
        System.out.println(t.height(t.root));
        System.out.println("minimum:");
        System.out.println(t.min(t.root));

    }

}
 class Trees{
    
    private class Node
    {
       private int value;
       private Node leftchild;
       private Node rightchild;

       public Node(int value)
       {
           this.value=value;
       }

       @Override
       public String toString()
       {
        return "Node="+value;

       }
    }

    Node root;
    public void insert(int value)
    {
        var node =new Node(value);
        if (root==null)
        {
            root=node;
            return;
        }
        var current=root;
        while(true){
            if(value<current.value)
            {
                if(current.leftchild==null)
                {
                    current.leftchild=node;
                    break;
                }
                current=current.leftchild;
            }
            else{
                if(current.rightchild==null)
                {
                    current.rightchild=node;
                    break;
                }
                current=current.rightchild;
            }
        }
    }
    

    public boolean find(Node root,int value)
    {
        Node current=root;
        if(root==null)
        {
            return false;
        }
        if(root.value==value )
        {
            return true;
        }
        if(current.value>value)
        {
           return find(current.leftchild,value);
        }
        else{
            return find(current.rightchild,value);
        }
       

    }

    public void preorder(Node root)
    {
        Node cur=root;
        if(root!=null)
        {
            System.out.println(cur.value);
            preorder(cur.leftchild);
            preorder(cur.rightchild);

        }
    }

    public void postorder(Node root){
        Node cur=root;
        if(root!=null)
        {
            postorder(cur.leftchild);
            postorder(cur.rightchild);
            System.out.println(cur.value);

        }
    }

    public void inorder(Node root){
        Node cur=root;
        if(root!=null)
        {
            inorder(cur.leftchild);
            System.out.print(cur.value);
            inorder(cur.rightchild);
        }
    }

  
  public int height(Node root)
   {
       if(root==null)
       {
           return -1;
       }
       if(root.leftchild==null && root.rightchild==null)
       {
           return 0;
       }
    return 1+Math.max((height(root.leftchild)),height(root.rightchild));
   }

   public int min(Node root)
   {
       if(root.leftchild==null && root.rightchild==null)
       {
           return root.value;
       }

       var left=min(root.leftchild);
       var right=min(root.rightchild);


       return(Math.min(Math.min(left,right),root.value));
   }

   
}
