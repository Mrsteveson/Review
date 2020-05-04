function sockMerchant(n, ar) {
    const colors = {};
    let matches = 0;

    for (let i = 0; i < n; i++) {
        if (colors[ar[i]]) {
            matches++;
            colors[ar[i]] = 0;
        } else {
            colors[ar[i]] = 1;
        }
    }
    
    return matches;
}