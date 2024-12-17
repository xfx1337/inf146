# infix to RPN

from Stack import Stack

priority = {
    "(": 0,
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
    "~": 4
}
def infix_to_RPN(exp):
    out = ""
    st = Stack()
    for i in range(len(exp.split())):
        w = exp.split()[i]
        if w not in "+-*/() ":
            out += f"{w} "
        elif w == "(":
            st.push(w)
        elif w == ")":
            while not st.is_empty and st.peek() != "(":
                out += f"{st.pop()} "
            st.pop()
        elif w in priority.keys():
            if (w == "-" and (i == 0 or (i>1 and exp[-1] in priority))):
                w = "~ "
            while not st.is_empty and priority[st.peek()] >= priority[w]:
                out += f"{st.pop()} "
            st.push(w)

    while not st.is_empty:
        out += f"{st.pop()} "
    return out

print(infix_to_RPN(input()))