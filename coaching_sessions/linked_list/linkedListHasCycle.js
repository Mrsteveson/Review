class Node {
    constructor(val, next_node=null) {
      this.val = val; 
      this.next = next_node; 
    }
  }
  ​
  function hasCycle(head) {
    let fast = head;
    let slow = head;
  ​
    while (fast && fast.next) {
      fast = fast.next.next; 
      slow = slow.next; 
  ​
      if (fast === slow) {
        return true;
      }
    }
  ​
    return false;
  }
  ​
  const n1 = new Node(1);
  const n2 = new Node(2);
  const n3 = new Node(3);
  const n4 = new Node(4);
  n1.next = n2;
  n2.next = n3;
  n3.next = n4;
  n4.next = n2;
  ​
  console.log(hasCycle(n1));