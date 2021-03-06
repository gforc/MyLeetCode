



class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", \
                       10: "X", 40: "XL", 50: "L", 90: "XC", \
                       100: "C", 400: "CD", 500: "D", 900: "CM", \
                       1000: "M"}
        keyset, result = sorted(numeral_map.keys()), []
        print(list(reversed(keyset)))
        print(list(sorted(numeral_map.keys())))
        while num > 0:
          
            for key in reversed(keyset):
                while num / key >= 1:
                    num -= key
                    result += numeral_map[key]
                    
        return "".join(result)

 
if __name__ == "__main__":
    print (Solution().intToRoman(999))
    print (Solution().intToRoman(3999))
