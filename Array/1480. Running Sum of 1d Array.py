"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""
from typing import List


def running_sum(nums: List[int]) -> List[int]:
    """
    The running_sum function takes a list of integers and returns the sum of all integers
    in the list up to and including that element.
    For example, if you pass it [3, 5, 2] as input it will return [3, 8, 10] as output.

    @param nums:List[int]: Pass in the list of numbers that will be summed
    return: The running sum of a list
    """
    result = []
    for i in range(len(nums)):
        arr = nums[0:i + 1]
        result.append(sum(arr))
    return result


print(running_sum([1, 1, 1, 1, 1]))
print(running_sum([3, 1, 2, 10, 1]))


def running_sum_2(nums: List[int]) -> List[int]:
    """
    The running_sum function takes a list of integers and returns the sum of all integers
    in the list up to and including that element.
    For example, if you pass it [3, 5, 2] as input it will return [3, 8, 10] as output.

    @param nums:List[int]: Pass in the list of numbers that will be summed
    return: The running sum of a list
    """
    sum_of = 0
    result = []
    for i in nums:
        sum_of += i
        result.append(sum_of)
    return result


print(running_sum_2([1, 1, 1, 1, 1]))
print(running_sum_2([3, 1, 2, 10, 1]))
