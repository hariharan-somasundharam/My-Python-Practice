from collections import defaultdict
def groupAnagrams(strs):
        Map = defaultdict(list)
        ans = []

        for s in strs:
            s_sorted = tuple(sorted(s))
            Map[s_sorted].append(s)
        
        for value in Map.values():
            ans.append(value)
        
        return ans
strs = ["nat","tea","tan","bat","ate", "eat"]
print(groupAnagrams(strs))