def isBalanced(s):
    stack = []
    bracketDict = {
        "}" : "{",
        "]" : "[",
        ")" : "("
    }
    for b in s:
        if b in bracketDict andstack and bracketDict[b] == stack[-1]:
            stack.pop()
        else:
            stack.append(b)

    if stack:
        return("NO")
    else:
        return("YES")