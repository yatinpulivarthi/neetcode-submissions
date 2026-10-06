class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max_water = 0;
        int left = 0;
        int right = heights.size() - 1;

        while(left < right){
            int width = right - left;
            int curr_height = min(heights[left], heights[right]);
            int curr_area = width * curr_height;
            max_water = max(max_water, curr_area);

            if(heights[left] < heights[right]){
                left++;
            }
            else{
                right--;
            }
        }
        return max_water;
    }
};
