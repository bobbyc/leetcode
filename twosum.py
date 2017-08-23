class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i] :
                    return [ i, j ];

    def twoSumII(self, numbers, target):
        l = 0
        r = len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

def main():
    try:
        s = Solution()
        answer = s.twoSumII([2, 7, 11, 15], 9)
        print(answer)
        answer = s.twoSumII([2, 7, 11, 15, 100], 26)
        print(answer)
        answer = s.twoSumII([-1, 2, 7, 11, 15], 10)
        print(answer)
    except Exception as e:
        exit(1)

if __name__ == '__main__':
    main()
