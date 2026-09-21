class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            if item in ["(", "[", "{"]:
                stack.append(item)
            else:
                if not stack:
                    return False
                if item == ")":
                    if stack[-1] == "(":
                        stack = stack[:-1]
                    else:
                        return False
                elif item == "}":
                    if stack[-1] == "{":
                        stack = stack[:-1]
                    else:
                        return False
                elif item == "]":
                    if stack[-1] == "[":
                        stack = stack[:-1]
                    else:
                        return False

        if stack:
            return False
        else:
            return True

                