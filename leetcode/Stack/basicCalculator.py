

# Recursive Approach
# TC -> O(n)
# SC -> O(n)
# Approach
# encountering -> ( - start dfs; encountering -> ) - stopping dfs.
# recursive function 'dfs' should return sm and idx of ")"


# Stack Approach
# TC -> O(n)
# SC -> O(n)
# Approach
# Maintain a stack, where latest num and operation before the expression in the round brackets is stored. Once we
# calculate expression in the brackets, we are popping the operation (either 1 or -1), popping the latest num,
# and calculating a new sm; sm = latest_num + bracket_sm * operation. Afterward, when we encounter a new "(", we
# are storing sm and the latest operation in the stack, so that, after evaluating the expression in the brackets,
# we were able to perform a similar operation to the one described above.

class Solution:

    def calculate_recursive(self, s: str) -> int:

        if not s: return -1

        def dfs(bracket_idx):

            sm = 0
            next_operation = "+"
            while bracket_idx < len(s):
                modifier = 0
                if s[bracket_idx] == "(":
                    modifier, after_idx = dfs(bracket_idx + 1)
                    bracket_idx = after_idx
                elif s[bracket_idx] == "-" or s[bracket_idx] == "+":
                    next_operation = s[bracket_idx]
                elif s[bracket_idx] == ")":
                    return sm, bracket_idx
                elif s[bracket_idx] == " ":
                    bracket_idx += 1
                    continue
                else:
                    while s[bracket_idx].isdigit():
                        modifier = modifier * 10 + int(s[bracket_idx])
                        bracket_idx += 1

                    bracket_idx -= 1

                if next_operation == "-": sm -= modifier
                if next_operation == "+": sm += modifier

                bracket_idx += 1

            return sm, bracket_idx

        res, _ = dfs(0)
        return res

    def calculate(self, s: str) -> int:
        if not s: return -1
        n_stack = []

        i = 0
        sm = 0
        operation = 1
        while i < len(s):

            if s[i] == " ":
                i += 1
                continue
            elif s[i] == "(":
                n_stack.append(sm)
                n_stack.append(operation)
                sm = 0
                operation = 1
            elif s[i] == "+":
                operation = 1
            elif s[i] == "-":
                operation = -1
            elif s[i].isdigit():
                modifier = 0
                while i < len(s) and s[i].isdigit():
                    modifier = modifier * 10 + ord(s[i]) - 48
                    i += 1

                sm += modifier * operation
                i -= 1
            elif s[i] == ")":
                latest_operation = n_stack.pop() if n_stack else 1
                latest_nm = n_stack.pop() if n_stack else 0
                sm = latest_nm + sm * latest_operation
                i += 1
                continue

            i += 1

        return sm



if __name__ == "__main__":
    sln = Solution()
    print(sln.calculate("1 + 1"))
