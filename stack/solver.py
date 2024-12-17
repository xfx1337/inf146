from math import *
import re

from Stack import Stack
import operator

priority = {
    "(": 0,
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "~": 3
}

def ctg(a):
    return 1/tan(a)

TRIG_FUNCS = {
    "sin": sin,
    "cos": cos,
    "tg": tan,
    "ctg": ctg
}

def find_brackets(exp, st):
    stack = Stack()
    end = st
    found = False
    for i in range(st, len(exp)):
        if exp[i] == "(":
            stack.push("(")
            if not found:
                st = i+1
            found = True
        elif exp[i] == ")":
            stack.pop()
        if stack.is_empty and found:
            end = i
            break
    return st, end

# 5+ (8*71 + 123 /2 )-6 *(1 *2+ 5-   9)   * 2    +  5/7
def split_s(exp):
    for s in "+-*/()":
        i = 0
        while i < len(exp):
            if exp[i] == s:
                exp = exp[0:i] + " " + exp[i] + " " + exp[i+1:]
                i += 1
            i += 1
    
    for f in TRIG_FUNCS.keys():
        oc = [m.start() for m in re.finditer(f, exp)]
        for i in range(len(oc)):
            start, end = find_brackets(exp, oc[i])
            x = TRIG_FUNCS[f](eval_RPN(infix_to_RPN(exp[start:end])))
            exp = exp[0:oc[i]] + f" {x} " + exp[end+1:]

    return exp.split()

def infix_to_RPN(exp):
    out = ""
    st = Stack()
    exp_s = split_s(exp)
    for i in range(len(exp_s)):
        w = exp_s[i]
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
        elif x in op:
            a, b = st.pop(), st.pop()
            st.push(op[x](b,a))
        else:
            raise ValueError("корявое выражение, друг")

    return st.pop()

x = infix_to_RPN(input())
print(x)
print(eval_RPN(x))