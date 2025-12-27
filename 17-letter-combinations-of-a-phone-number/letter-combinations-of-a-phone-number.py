class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }

        result = [""]

        for digit in digits:
            temp = []
            for combo in result:
                for letter in phone[digit]:
                    temp.append(combo + letter)
            result = temp

        return result
