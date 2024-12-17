from Stack import Stack
import re

"""
t = 1+4*6 - (2+3*4)

инфиксная запись
a + b

префиксная
+a b

постфиксная
a b+

Обратная польская нотация RPN
Обычная: t = 1+4*6 - (2+3*4)
RPN: 3 4 * 2 + 4 6 * 1 + -

"""

def eval_RPN(t):
    st = Stack()
    t = t.split()
    for x in t:
        #if re.fullmatch(x, r"^[0-9.-]+$"): # if x is float

        if x not in "+-*/":
            st.push(float(x))
        else:
            a, b = st.pop(), st.pop()
            if x == "+":
                st.push(a+b)
            if x == "-":
                st.push(a-b)
            if x == "/":
                st.push(a/b)
            if x == "*":
                st.push(a*b)
    return st.pop()

print(eval_RPN(input()))