import java.util.*;

class Solution{
    public int solution(int[][] board, int[][] skill){
        int ans=0;
        int 행= board.length;
        int 열= board[0].length;
        int [][] ans_행렬= new int[행+1][열+1];


        for (int[] skills : skill) {
            if(skills[0]==2){
                ans_행렬[skills[1]][skills[2]]+=skills[5];
                ans_행렬[skills[1]][skills[4]+1]-=skills[5];
                ans_행렬[skills[3]+1][skills[2]]-=skills[5];
                ans_행렬[skills[3]+1][skills[4]+1]+=skills[5];
            }else{
                ans_행렬[skills[1]][skills[2]]-=skills[5];
                ans_행렬[skills[1]][skills[4]+1]+=skills[5];
                ans_행렬[skills[3]+1][skills[2]]+=skills[5];
                ans_행렬[skills[3]+1][skills[4]+1]-=skills[5];
            }

        }//아 검산이 안되는데 기억이 안나네

        for (int i = 0; i <행+1; i++) {
            for(int j=0;j<열;j++){
                ans_행렬[i][j+1]+=ans_행렬[i][j];
            }
        }

        for (int i = 0; i <열+1; i++) {
            for(int j=0;j<행;j++){
                ans_행렬[j][i+1]+=ans_행렬[j][i];
            }
        }

        for (int i = 0; i < 행; i++) {
            for (int j = 0; j < 열; j++) {
                if(ans_행렬[i][j]+ board[i][j]>0){
                    ans++;
                }
            }
        }

        return ans;


    }


}