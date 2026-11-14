# def rearrange_by_frequency(nums: list[int]) -> list[int]:
#     counts = {}
#     for num in nums:
#         counts[num] = counts.get(num, 0) + 1

#     return sorted(nums, key=lambda x: (-counts[x], x))


# # Testlar
# print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))
# # Natija: [4, 4, 4, 5, 5, 3, 6]

from collections import Counter


def rearrange_by_frequency(nums: list[int]) -> list[int]:
    # Har bir sonning uchrash chastotasini hisoblaymiz
    chastotalar = Counter(nums)

    # Chastota bo'yicha kamayish, qiymat bo'yicha o'sish tartibida saralaymiz
    return sorted(nums, key=lambda son: (-chastotalar[son], son))


# Testlar
print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))
# Kutilgan natija: [4, 4, 4, 5, 5, 3, 6]