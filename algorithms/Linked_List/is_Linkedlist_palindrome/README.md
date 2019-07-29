### Check if the given linked list is palindrome or not.

This method functions recursively using two pointers:
	keep `slow` pointer on head and `cur` pointer on second last node. Check if value of slow node and last node (`cur.next`) is equal.
	if equal: delete last node i.e `cur.next=None` as we dont need it any more. move `slow` pointer to next node. call `isPalindrome(slow)` recursively and it will return True when it comes to base case.
	else : return False

### Input Format:
First line of input contains number of testcases t. For each testcase, first line of input contains length of linked list N and next line contains N integers as data of linked list.

### Output Format:
For each test case output will be 1 if the linked list is a palindrome else 0.

### Task:
The task is to complete the function isPalindrome() which takes head as reference as the only parameter and returns true or false if linked list is palindrome or not respectively.

### Sample Input:
```
2
3
1 2 1
4
1 2 3 4
```
### Sample Output:
```
1
0
```

### Explanation:
# Testcase 1:
 1 2 1 is palindrome
# Testcase 2:
 1 2 3 4 is not equal to its reversed Linked list 4 3 2 1

### Implemented in:
- [Python](isPalindrome.py)



