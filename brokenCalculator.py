"""
Forward moves are x*2 or x-1. Min steps come from working backwards from target to startValue
Reverse moves: if target is even, best is to halve it; if odd, increment it (to make it even)
Once target ≤ start, only option is to decrement start down: add start - target
"""
"""
Time Complexity: O(log target) 
Space Complexity: O(1)
"""

class brokenCalculator:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ops = 0
        while target > startValue:
            ops += 1
            if target % 2 == 0:
                target //= 2     # reverse of doubling
            else:
                target += 1      # reverse of decrement
        return ops + (startValue - target)

if __name__ == "__main__":
    s = brokenCalculator()
    print(s.brokenCalc(2, 3))    
    print(s.brokenCalc(5, 8))    