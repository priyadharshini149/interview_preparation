
import java.util.*;



public class Tree {
    public static void main(String args[])
    {
        Trees t =new Trees();
        Trees t1 =new Trees();
        t.insert(7);
        t.insert(4);
        t.insert(9);
        t.insert(1);
        t.insert(6);
        t.insert(8);
        t.insert(10);


        t1.insert(7);
        t1.insert(4);
        t1.insert(9);
        t1.insert(1);
        t1.insert(6);
        t1.insert(8);
        t1.insert(10);

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

        System.out.println(t.equals(t.root,t1.root));
        // t.swap(t.root);
        System.out.println("bst or not:"+t.isBinarySearchTree(t.root, Integer.MIN_VALUE,Integer.MAX_VALUE));
        List<Integer> list=new ArrayList<Integer>();
       
       List<Integer>l= t.kdistance(t.root,2,list);
       System.out.println(l);
       for(int item:l)
       System.out.println(item);
       System.out.println("level order");
       t.traversalLevelorder();
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
    Node node =new Node(value);
        if (root==null)
        {
            root=node;
            return;
        }
        Node current=root;
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

   public int min(Node root)//o(n)
   {
       if(root.leftchild==null && root.rightchild==null)
       {
           return root.value;
       }

       int left=min(root.leftchild);
     int right=min(root.rightchild);
       return(Math.min(Math.min(left,right),root.value));
   }
  
   public int min()//in bst time complexity o(logn)
   {
      Node cur=root;
      Node last=cur;
      if(root==null)
      {
          throw new IllegalStateException();
      }
      while(cur!=null)
      {
          last=cur;
          cur=cur.leftchild;
      }
      return last.value;
   }

public boolean equals(Node first,Node second)
{
    if(second==null ||first==null){
        return false;
    }
    if(first==null && second==null)
    {
        return true;
    }
    if(first!=null && second!=null )
    {
        return first.value==second.value && equals(first.leftchild,second.leftchild)  &&  equals(first.rightchild,second.rightchild);
    }
  return false;

}
   
public boolean isBinarySearchTree(Node root,int min,int max)
{
if(root==null)
 return true;
 if(root.value<min||root.value>max)
 return false;
 return isBinarySearchTree(root.leftchild,min,root.value-1) &&  isBinarySearchTree(root.rightchild,root.value+1,max);
}
public void swap(Node root)
{
    Node temp=root.leftchild;
    root.leftchild=root.rightchild;
    root.rightchild=temp;
}


public ArrayList<Integer> kdistance(Node root,int distance,List<Integer> list)
{
    
    if(root==null)
    {
        return new ArrayList<>();
    }
    if(distance==0)
    {
        list.add(root.value);
       

    }
    kdistance(root.leftchild, distance-1,list);
    kdistance(root.rightchild, distance-1,list);
    return (ArrayList<Integer>) list;
}

public void traversalLevelorder()
{
    List<Integer>l=new ArrayList<Integer>();
    List<List<Integer>>res=new ArrayList<List<Integer>>();
    for (int i=0;i<=height(root);i++)
    {
       l=kdistance(root, i,new ArrayList<Integer>());
   
    res.add(l);
    
    }
    System.out.println(res);
}



}
