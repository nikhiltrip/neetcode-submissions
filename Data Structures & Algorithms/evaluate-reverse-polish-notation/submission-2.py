class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = []
        nums = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                operators.append(token)
                if len(nums) >= 2:
                    if token == "+":
                        nums[len(nums) - 2] += nums[len(nums) - 1]
                        del nums[len(nums) - 1]
                        operators.pop()
                    if token == "-":
                        nums[len(nums) - 2] -= nums[len(nums) - 1]
                        del nums[len(nums) - 1]
                        operators.pop()
                    if token == "*":
                        nums[len(nums) - 2] *= nums[len(nums) - 1]
                        del nums[len(nums) - 1]
                        operators.pop()
                    if token == "/":
                        nums[len(nums) - 2] = int(nums[len(nums) - 2]/nums[len(nums) - 1])
                        del nums[len(nums) - 1]
                        operators.pop()
            else:
                nums.append(int(token))
            
        return nums[0]
            