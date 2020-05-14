// Singly-linked lists are already defined with this interface:
// struct List<T> {
//     value: T,
//     next: Option<Box<List<T>>>
// }
// impl<T> List<T> {
//     fn new(v : T) -> Self {
//         List { value: v, next: None }
//     }
// }
// type ListNode<T> = Option<Box<List<T>>>;
//
​
fn list_len(l: &ListNode<i32>) -> usize {
    let mut count = 0;
    let mut ptr = l.as_ref();
​
    while let Some(node) = ptr {
        count += 1;
        ptr = node.next.as_ref();
    }
​
    count
}
​
fn isListPalindrome(l: ListNode<i32>) -> bool {
    // get list length
    let len = list_len(&l);
​
    // ahead and behind pointers
    let mut al = l;
    let mut bl = None;
​
    // advance the ahead pointer, reversing the list as we go
    for _ in 0..(len / 2) {
        if let Some(mut node) = al {
            al = node.next.take();
            node.next = bl;
            bl = Some(node);
        }
    }
​
    // check to see if we have a list with an odd number of nodes
    if len % 2 == 1 {
        // advance the ahead pointer once to skip the odd element
        al = al.unwrap().next;
    }
​
    // traverse ahead and behind pointers in unison
    while let (Some(n1), Some(n2)) = (al, bl) {
        if n1.value != n2.value { return false; }
        
        al = n1.next;
        bl = n2.next;
    }
​
    true
}