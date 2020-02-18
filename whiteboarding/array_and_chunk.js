// --- Directions
// Given an array and chunk size, divide the array into many subarrays
// where each subarray is of length size

// --- Examples
// chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
// chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
// chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
// chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
// chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

// Solution One
function chunk(array, size) {
	let chunked = []
	
	for(let i = 0; i < array.length; i+=size){
		chunked.push(array.slice(i, i + Math.min(size, array.length - i)))
	}
	return chunked
}

// Solution two
function chunk(array, size) {
    let chunked = []
    for(let item of array){
        let lastItem = chunked[chunked.length - 1]
        if(!lastItem || lastItem.length === size){
            chunked.push([item])
        }else{
            lastItem.push(item)
        }
    }
    return chunked
}

// Notes
// array slice
// while length of array is === target size  or for loop where we increment by chunk size
// index will be starting point of slice for array 2
// will need length remaining and chunk size