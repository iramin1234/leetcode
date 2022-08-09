class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer,Integer> tracker = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            if(!tracker.containsKey(nums[i])){
                tracker.put(nums[i], 1);
            }
            else{
                return true;
            }
        }
        return false;
    }
}