
# TC -> O(n)
# SC -> O(n)

# Approach: Stack

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for a in asteroids:
            if a >= 0:
                stack.append(a)
            else:
                while stack and stack[-1] >= 0 and abs(a) > stack[-1]:
                    stack.pop()

                if stack and stack[-1] == abs(a):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(a)

        return stack