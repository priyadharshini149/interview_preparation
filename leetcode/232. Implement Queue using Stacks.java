class MyQueue {

    Stack<Integer> s1;
    Stack<Integer> s2;
    public MyQueue() {
        
       this.s1=new Stack<Integer>();
       this.s2=new Stack<Integer>();
    }
    
    public void push(int x) {
       
        this.s1.push(x);
        
    }
    
    public int pop() {
        
        while(this.s1.size()>1)
        {
            this.s2.push(this.s1.pop());
        }
        int res=this.s1.pop();
        while(this.s2.size()>0)
        {
            this.s1.push(this.s2.pop());
        }
        return res;
        
    }
    
    public int peek() {
        return this.s1.get(0);
    }
    
    public boolean empty() {
        
        return this.s1.empty();
        
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */