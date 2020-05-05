function main() {
    var i = 4
    var d = 4.0
    var s = "HackerRank "
    // Declare second integer, double, and String variables.
    let i2, d2, s2
    // Read and save an integer, double, and String to your variables.
    i2 = parseInt(readLine());
    d2 = parseFloat(readLine());
    s2 = readLine();
    // Print the sum of both integer variables on a new line.
    console.log(i2 + i);
    // Print the sum of the double variables on a new line.
    console.log((d2 + d).toFixed(1));
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    console.log(s + s2);
}