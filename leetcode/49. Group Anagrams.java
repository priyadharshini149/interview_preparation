class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>>mp=new HashMap<>();
    for(String s:strs)
    {
        char[] chArray=s.toCharArray();
        Arrays.sort(chArray);
        String str=new String(chArray);
        System.out.println(str);
        if(mp.containsKey(str)==false)
        {
            mp.put(str,new ArrayList<>());
        }
        for(Map.Entry x:mp.entrySet())
        {
            System.out.println(x.getValue());
        }
        System.out.println(mp.get(str));
        mp.get(str).add(s);
    }
        List<List<String>> ans=new ArrayList<>(mp.values());
        return ans;
    
    
    }
}