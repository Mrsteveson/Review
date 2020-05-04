function frequencyQueries(queries) {
    const answers = [];
    // keeps track of the number of occurrences of eacy query value 
    const occurrences = {};
    // keeps track of how many values have shown up a certain number of times
    // keys are integers representing frequency and values are the number 
    // of values that showcase that frequency 
    // for example, if a query specifies a new value, then that value has 
    // only shown up once, so we'll increment the value associated with 
    // the key of 1 to indicate that there is an additional value that 
    // has shown up once 
    const frequencies = {};
​
    for (const [op, val] of queries) {
        if (op === 1) {
            // subtract an occurrence of the value's prior frequency 
            frequencies[occurrences[val]]--;
            // add the value to our occurrences map 
            occurrences[val] = (occurrences[val] || 0) + 1;
            // increment an occurrence of the value's new frequency 
            frequencies[occurrences[val]] = (frequencies[occurrences[val]] || 0) + 1;
        } else if (op === 2 && occurrences[val]) {
            // subtract an occurrence of the value's prior frequency 
            frequencies[occurrences[val]]--; 
            // remove the value from our occurrences map 
            occurrences[val]--;
            // increment an occurrence of the value's new frequency 
            frequencies[occurrences[val]]++;
        } else if (op === 3) {
            // all we have to do for operation 3 is check if the value 
            // associated with the frequency > 0 
            answers.push(frequencies[val] > 0 ? 1 : 0);
        }
    }
​
    return answers;
}
