from Stack import Stack
import re
import operator

"""
t = 1+4*6 - (2+3*4)

инфиксная запись
a + b

префиксная
+a b

постфиксная
a b+

Обратная польская нотация RPN
Обычная: t = 1 + 4 * 6 - ( 2 + 3 * 4 )
RPN: 3.2 4 * 2 + 4 6 * 1 + -

"""

op = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def eval_RPN(t):
    st = Stack()
    t = t.split()
    for x in t:
        if x not in "*/+-": # if x is float
            st.push(float(x))
        #breakpoint()
        #if re.fullmatch(x, r"^[0-9.-]+$"):
        #    st.push(float(x))
        elif x in op:
            a, b = st.pop(), st.pop()
            st.push(op[x](a,b))
        else:
            raise ValueError("корявое выражение, друг")

    return st.pop()

print(eval_RPN(input()))