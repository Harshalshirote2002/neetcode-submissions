class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "\n"
        if len(strs) == 0:
            return "[]"

        return encoded.join(strs)

        # for s in strs:
        #     encoded += s
        #     encoded = encoded + len(s)+ "\n"
        # return encoded
        

    def decode(self, s: str) -> List[str]:
        
        if s == "[]":
            return []
        elif s:
            return s.split("\n")
        else:
            return [""]

