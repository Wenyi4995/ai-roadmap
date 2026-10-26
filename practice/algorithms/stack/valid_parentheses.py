"""有效的括号：使用栈检查括号是否正确配对。"""


def is_valid(text):
    stack = []

    pairs = {
        ")":"(",
        "]":"[",
        "}":"{"
    }


    for char in text:
        if char in "([{":
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()

            if top != pairs[char]:
                return False

    return len(stack) == 0


assert is_valid("()") is True
assert is_valid("()[]{}") is True
assert is_valid("(]") is False
assert is_valid("([)]") is False
assert is_valid("{[]}") is True

print("所有测试通过")
