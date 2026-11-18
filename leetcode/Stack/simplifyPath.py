
# n -> len(path)
# TC -> O(n)
# SC -> O(n)


class Solution:
    def simplifyPath(self, path: str) -> str:
        splitted_path = path.split("/")
        stack = []

        for part in splitted_path:
            if stack and part == "..":
                stack.pop()
            elif not part or part == "." or part == "..":
                continue
            else:
                stack.append(part)

        return "/" + "/".join(stack)