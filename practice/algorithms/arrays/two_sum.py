"""两数之和：使用字典在一次遍历中寻找答案。"""


def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        number = nums[i]
        needed = target - number

        if needed in seen:
            return [seen[needed], i]

        seen[number] = i

    return []


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([5, 5, 2, 9], 11) == [2, 3]
assert two_sum([3, 3], 6) == [0, 1]

print("所有测试通过")
