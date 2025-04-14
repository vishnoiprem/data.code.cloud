class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = ['(', '{', '[']
        close = [')', '}', ']']
        open_close = list(zip(open, close))
        stack = []
        for k, v in enumerate(s):
            if v in open:
                stack.append(v)
            elif v in close:
                if len(stack)<1:
                    return False
                pop=stack.pop()
                if (pop,v) not in open_close:
                    return False
        if len(stack)<1:
            return True
        else:
            return False
s = "()[]{}"
print(Solution().isValid(s))
