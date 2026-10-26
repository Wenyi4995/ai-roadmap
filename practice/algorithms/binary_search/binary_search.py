"""二分查找：在升序数组中寻找目标值的下标。"""


def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        middle = (low + high) // 2
        if target == nums[middle]:
            return middle
        if target > nums[middle]:
            low = middle + 1
        if target < nums[middle]:
            high = middle - 1
    # TODO 1：创建左右边界 left 和 right。
    # TODO 2：在 left <= right 时反复检查中间位置。
    # TODO 3：根据比较结果缩小左半区或右半区。
    # 找不到时返回 -1。
    return -1



assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
assert binary_search([5], 5) == 0
assert binary_search([5], 1) == -1

print("所有测试通过")
