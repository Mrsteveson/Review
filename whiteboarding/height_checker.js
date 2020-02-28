// https://leetcode.com/problems/height-checker/


let heights = [1,1,4,2,1,3]
let heightChecker = function(heights) {
    let count=0;
    let arr=heights.slice().sort((a,b)=> a-b);
    for(i=0; i<heights.length; i++){
        if(heights[i]!==arr[i]) count++;
    }
    return count;
};
console.log(heightChecker(heights));