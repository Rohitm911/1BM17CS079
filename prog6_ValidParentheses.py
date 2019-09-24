class validString:
    def __init__(self, s):
        self.s = s
    def checkString(self):
        stack = []
        s1 = self.s[1:]
        s2 = self.s[0]
        stack.append(s2)
        for ch in s1:
            if (ch == '}' and  stack[-1] == '{'):
                stack.pop()
            elif ( ch == ')' and stack[-1] == '('):
                stack.pop()
            elif (ch == ']' and  stack[-1] == '['):
                stack.pop()
            else:
                stack.append(ch) 
        if len(stack) == 0:
            return True
        else:
            return False

s = input("Enter the String : ")
validateString = validString(s)
if validateString.checkString():
    print ("Valid String")
else:
    print ("Invalid String")
            
