"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money
the ith customer has in the j bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.


Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation:
1st customer has wealth = 6
2nd customer has wealth = 10
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17


Constraints:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100
"""
from typing import List


def maximum_wealth(accounts: List[List[int]]) -> int:
    """
    The maximum_wealth function will take a list of lists and return the maximum wealth
    of all the children in a family. The function will iterate through each sublist and
    add the values together, if one child has more money than another it will be
    returned as the maximum wealth.

    N - length of list
    M - length child list
    Time Complexity: O(N * M)
        As the length of N and length of M varies so the no of iterations for each list
        varies.
    Space Complexity: O(1)
        As we are having only two variables child_sum and max_child so no matter the
        length of N or M. It will be always 8 bytes.

    @param accounts: Store the accounts of all the children
    return: The maximum sum of money that can be made by a child
    """
    max_child = 0
    for i in accounts:
        child_sum = sum(i)
        if child_sum > max_child:
            max_child = child_sum
    return max_child


print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))
print(maximum_wealth([[1, 5], [7, 3], [3, 5]]))
print(maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))


def maximum_wealth_2(accounts: List[List[int]]) -> int:
    """
    The maximum_wealth_2 function takes a list of lists and returns the maximum wealth
    of any child in the family. The accounts' parameter is a list of lists where each
    inner list contains two integers, one for the child's name and one for their bank
    account balance. The function will return an integer representing the maximum
    balance across

    N - length of list
    M - length child list
    Time Complexity: O(N * M)
        As the length of N and length of M varies so the no of iterations for each list
        varies.
    Space Complexity: O(1)
        As we are having only one variable max_child so no matter the length of N or M.
        It will be always 4 bytes.

    @param accounts: Represent a list of accounts
    return: The maximum wealth of the child in each account
    """
    max_child = 0
    for i in accounts:
        max_child = max(max_child, sum(i))
    return max_child


print(maximum_wealth_2([[1, 2, 3], [3, 2, 1]]))
print(maximum_wealth_2([[1, 5], [7, 3], [3, 5]]))
print(maximum_wealth_2([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
