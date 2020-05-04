function isListPalindrome(l) {
    if(!l) return true
​
    //rabbit hair method
    //thre pointers
    let slow = l  // will be reversed
    let fast = l.next  //used to stop slow at middle
    let slowB = l // will continue forward
    let p = null
    let even = true
    //in while loop (while faster is not null)
    while(fast) {
        //reversing LL
        let n = slow.next
        slow.next = p
        p = slow
​
        //slow moves by 1
        //fast moves by 2
        // if statement to handle even/odd lengths
        if(fast.next) {
            fast = fast.next.next
            slow = n
            //used later to continue traversal
			slowB = n.next
			
			//if fast is now null, reverse pointer here b/c while stops
            if(!fast) {
                slow.next = p
            }
			
            even = false
        } else {
            fast = fast.next
            //used later to continue traversal
            slowB = n
            even = true
        }
    }
​
    if(!even) slow = slow.next
​
    // slow now does reversed traversal while slowB continues forward
    while(slow) {
        if(slow.value !== slowB.value) return false
        slow = slow.next
        slowB = slowB.next
    }
    return true
}
