#https://leetcode.com/problems/sort-array-by-parity/
class Solution {
    public int[] sortArrayByParity(int[] A) {
        int h=0,t=A.length-1;
        int[] R = new int[A.length];
        for(int i=0; i<A.length; i++){
            if(A[i] % 2 == 0){
                R[h] = A[i];
                h++;
            }
            else{
                R[t] = A[i];
                t--;
            }
        }
        return R;
    }
}
