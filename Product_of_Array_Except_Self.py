class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answers = [1] * n

        before = 1
        for i in range(n):
            answers[i] = before
            before *= nums[i]

        after = 1
        for i in range(n - 1, -1, -1):
            answers[i] *= after
            after *= nums[i]

        return answers
