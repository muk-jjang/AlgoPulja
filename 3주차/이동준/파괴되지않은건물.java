import java.util.*;
//흠... 길이 1000? skill 250,000? 할만한데?
//공격이냐 회복이냐..-> 함수 2개 쓸까 1개쓰고 트리거를 나눌까
//10초..
//살아 있는걸 하나하나 다 세도 효율이 나올까? 흠... 마이너스를 세야하나? 상황마다 두개를 나눈다? 흠 비효율적인데 고민..
// 누적합?... 그걸로 효율이 다 나오나..
//2차원 누적합으로 풀어봤는데 타임에러 뜸 ㅅㅂ
//누적합 오랜만에 구현하려니 머리 터질거 같음 다시 공부해야 겠다
// 2차원 누적합 두번 생각해ㅑ해서 너무 어렵네
//아니 이것도 안풀리는데 어떻게 푸냐
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