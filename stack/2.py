from Stack import Stack

REPLACE = {"<": ">", "(": ")", "[": "]", "{": "}", None: None}
s = input("input:")
st = Stack()

status = True
for x in s:
    if x in REPLACE.keys():
        st.push(x)
    if x in REPLACE.values():
        if REPLACE[st.pop()] != x:
            status = False
            break
if not st.is_empty:
    status = False
print(status)