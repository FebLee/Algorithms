class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing(num):
            num_origin = num
            while num > 0:
                remainder = num % 10
                # 
                if remainder == 0 or num_origin % remainder != 0:
                    return False
                num = num // 10
            return True       
        
        return [i for i in range(left, right+1) if is_self_dividing(i)]

##solution 2
class Solution:
    def __init__(self, n):
        self.n = n;
        
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [i for i in range(left, right+1) if self.is_self_dividing(i)]               
                    
    def is_self_dividing(self, num):
        num_origin = num
        while num > 0:
            remainder = num % 10
            # Importantly, put reminder ahead
            if remainder == 0 or num_origin % remainder != 0:
                return False
            num = num // 10
        return True
