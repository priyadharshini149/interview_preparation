class Solution {
    public List<Integer> partitionLabels(String s) {
        int limit=0;
        HashMap<Character,Integer> obj=new HashMap<>();
        ArrayList<Integer> res=new ArrayList<>();
        for(int i=0;i<s.length();i++)
        {
            obj.put(s.charAt(i),i);
        }
        int sum=0;
        for(int i=0;i<s.length();i++)
        {
            limit=Math.max(obj.get(s.charAt(i)),limit);
            System.out.print(limit);
            if(i==limit)
            {           
                res.add((limit+1)-sum);
                System.out.print(res);
                 sum=limit+1;
            }
        }
        return res;
    }
}
