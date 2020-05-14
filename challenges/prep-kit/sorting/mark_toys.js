function maximumToys(prices, k) {
    let sum = 0;
    let sorter = prices.sort((a, b) => a - b);
    let counter = 0

    for (var i = 0; i < sorter.length; i++){
            if (sorter[i] < k){
                sum += sorter[i]
                if (sum <= k){
                    counter++
                }
            }
    }
    console.log(counter)
}