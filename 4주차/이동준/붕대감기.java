//bandage : [시전 시간, 초당 회복량, 추가 회복량]
//attacks: [공격 시간, 피해량]
//health : 목숨
//연속 성공 그 순간에 추가 회복함
//최대 최력 초과x
//공격 당할때 회복x
//공격시간 오름차순 정렬로 되어있음
//공격시간 무조건 다 다름 휴


class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int Cont_Healing=0; //연속 회복 횟수
        int life=health; //목숨
        int attack_index=0; //공격 횟수
        int Last_attack= attacks[attacks.length-1][0]; //마지막 공격 시간
        for(int i=1;i<=Last_attack;i++){
            if(attacks[attack_index][0]==i){ //공격 타임
                life-=attacks[attack_index][1];  //체력 감소
                attack_index+=1;
                Cont_Healing=0; //연속 힐링 리셋
                if(life<=0){
                    return -1;
                }
            }
            else {  //공격x
                if(life<health){  //원래 체력보다 지금 목숨 낮은 경우
                    Cont_Healing++;
                    life+=bandage[1];
                    if(Cont_Healing==bandage[0]){ //추가체력회복
                        life+=bandage[2];
                        Cont_Healing=0;  //리셋 필수
                    }
                    if(life>health){  //체리
                    }
                }

            }
        }

        return life;
    }


}