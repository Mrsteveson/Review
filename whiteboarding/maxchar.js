// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

function maxChar(str) {
    let obj = {}
    for(let char of str){
      if(!obj[char]){
          obj[char] = 1
      } else {
          obj[char] += 1
      }
    }
    return Object.keys(obj).reduce((a, b) =>{
         return  obj[a] > obj[b] ? a : b})
}


// create an variable that is an object 
// if its not in the object, set the value to one, otherwise add that entry
// once we get the dictionary, find the max value and then return the character that corresponds to that value