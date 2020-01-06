#https://leetcode.com/problems/sort-array-by-parity-ii/
class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int e_index=0,o_index=1;
        int[] R = new int[A.length];
        for(int i=0; i<A.length; i++){
            if(A[i]%2 == 0){
                R[e_index] = A[i];
                e_index += 2;
            }
            else{
                R[o_index] = A[i];
                o_index += 2;
            }
        }
        return R;
    }
}
