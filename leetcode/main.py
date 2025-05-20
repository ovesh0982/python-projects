'''
# QUESTION :- how to find the two sum using target base in list
class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

# Example usage
if __name__ == "__main__":
    solution = Solution()  # Create an instance of Solution
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)  # Call the method on the instance
    print(result)  # Output: [0, 1]
'''

'''
# QUESTION :- find the roman number alphabate
def roman_to_integer(s: str)->int:
    roman_numerals = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
    }
    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
        
    return total


roman_number = "MCMXCIV"
integer_value = (roman_to_integer(roman_number))
print(integer_value)
'''


'''
# find the number of digits
def letter_combinations(digits):
    if not digits:
        return []
    
    digit_to_letters = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }

    def backtrack(index,path):
        if index == len(digits):
            combinations.append("".join(path))
            return

        possible_letters = digit_to_letters[digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1,path)
            path.pop()

    
    combinations = []
    backtrack(0,[])
    return combinations

phone_number = "23"
print(letter_combinations(phone_number))
'''



# 3. Longest Substring Without Repeating Characters
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.



    
