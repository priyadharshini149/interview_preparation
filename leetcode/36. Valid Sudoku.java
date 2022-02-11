class Solution {
    public boolean isValidSudoku(char[][] board) {
        
        int[][] row=new int[9][10];
        int [][] col=new int[9][10];
        
        int[][][] cube=new int[3][3][10];
        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                if(board[i][j]=='.') continue;
                int x=board[i][j]-'0';
                if(row[i][x]>0) return false;
                row[i][x]++;
                
                if(col[j][x]>0) return false;
                col[j][x]++;
                
                if(cube[i/3][j/3][x]>0) return false;
                cube[i/3][j/3][x]++;
                
            }
        }
        
        return true;
            
    }
}