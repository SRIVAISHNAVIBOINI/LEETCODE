class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        num=0
        cs=""
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                st.append((cs, num))
                cs = ""
                num = 0

            elif ch == ']':
                prev, repeat = st.pop()
                cs = prev + cs * repeat

            else:
                cs += ch

        return cs
        