class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map_dict = {}

        keys = set(s1)

        n = len(s1)

        for char in s1:
            if char in map_dict.keys():
                map_dict[char] += 1
            else:
                map_dict[char] = 1
            
        if len(s1)>len(s2):
            return False

        l = 0
        r = n -1

        while r < len(s2):
            part = s2[l:r+1]

            part_dict = {}

            for char in part:
                if char in map_dict.keys():
                    if part_dict.get(char):
                        part_dict[char]+=1
                    else:
                        part_dict[char]=1


            if part_dict == map_dict:
                return True

            r+=1
            l+=1

            
        return False
                
            

        