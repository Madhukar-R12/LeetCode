class Solution:
    def calPoints(self, operations: List[str]) -> int:
    # more efficient method 1
        stack = []
        for i in operations:
            if i=="C":
                stack.pop()
            elif i=="D":
                stack.append(stack[-1]*2)
            elif i=="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)
    
    #My own method -2

        stack = [x for x in operations[::-1]]
        l = []
        for j in range(len(stack)):
            res = stack.pop()
            if (res.isdigit()):
                l.append(int(res))
            elif res=="C":
                l.pop()
            elif res=="D":
                l.append(l[-1]*2)
            elif res=="+":
                l.append(l[-1]+l[-2])
            else:
                l.append(int(res))
        return sum(l)