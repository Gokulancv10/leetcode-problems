"""
1929. Concatenation of Array

Given an integer array nums of length n, you want to create an array ans of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.


Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]


Constraints:

n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000
"""
from typing import List


def get_concatenation(nums: List[int]) -> List[int]:
    """
    The get_concatenation function takes a list of integers and returns the
    concatenation of all the numbers in the list.
    For example, if nums = [3, 2, 1], then get_concatenation(nums) should return 321.

    Time Complexity: O(n)
    Space Complexity: O(n)

    n - length of array/list
    Input Size: 4n bytes
    Auxiliary Space: 4n + 12 bytes

    @param nums:List[int]: Store the list of numbers that are passed into the function
    return: A concatenation of the list
    """
    result = []
    for i in nums:
        result.append(i)
    for i in nums:
        result.append(i)
    return result


print(get_concatenation([1, 2, 1]))
print(get_concatenation([1, 3, 2, 1]))


def get_concatenation_2(nums: List[int]) -> List[int]:
    """
    The get_concatenation function takes a list of integers and returns the
    concatenation of all the numbers in the list.
    For example, if nums = [3, 2, 1], then get_concatenation(nums) should return 321.

    Time Complexity: O(n)
    Space Complexity: O(n)

    n - length of array/list
    Input Size: 4n bytes
    Auxiliary Space: 4n + 12 bytes

    @param nums:List[int]: Store the list of numbers that are passed into the function
    return: A concatenation of the list
    """
    n = len(nums)
    result = [0] * (2 * n)
    for i in range(len(nums)):
        result[i] = nums[i]
        result[i + n] = nums[i]
    return result


print(get_concatenation_2([1, 2, 1]))
print(get_concatenation_2([1, 3, 2, 1]))


def get_concatenation_3(nums: List[int]) -> List[int]:
    """
    The get_concatenation function takes a list of integers and returns the
    concatenation of all the numbers in the list.
    For example, if nums = [3, 2, 1], then get_concatenation(nums) should return 321.

    Time Complexity: O(1)
    Space Complexity: O(1)

    n - length of array/list
    Input Size: 4n bytes
    Auxiliary Space: 4 bytes

    @param nums:List[int]: Store the list of numbers that are passed into the function
    return: A concatenation of the list
    """
    return nums + nums


print(get_concatenation_3([1, 2, 1]))
print(get_concatenation_3([1, 3, 2, 1]))
