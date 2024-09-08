// Given the head of a singly linked list, reverse the list, and return the reversed list.

// Example 1:

// Input: head = [1,2,3,4,5]
// Output: [5,4,3,2,1]
// Example 2:

// Input: head = [1,2]
// Output: [2,1]
// Example 3:

// Input: head = []
// Output: []

// Constraints:

// The number of nodes in the list is the range [0, 5000].
// -5000 <= Node.val <= 5000

var reverseList = function (head) {
  let prev = null;
  let current = head;

  while (current !== null) {
    let nextNode = current.next; // Store the next node
    current.next = prev; // Reverse the link
    prev = current; // Move prev to current
    current = nextNode; // Move current to the next node
  }

  return prev; // Prev is the new head of the reversed list
};
