

def twoSum(nums=('2','7','11','15'), target=9):
    lst = []
    if len(nums) <= 2 and sum(nums) == target:
        return [0, 1]
    else:
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and nums[i] not in lst and nums[j] not in lst:
                    lst.append(nums.index(nums[i]))
                    lst.append(nums.index(nums[j]))
        return lst


print(twoSum())
