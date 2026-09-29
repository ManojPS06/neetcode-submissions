class Solution:
    def groupAnagrams(self, string_list: List[str]) -> List[List[str]]:
        mapping_dict = defaultdict(list) 
        #mapping_dict = {'act': [], 'opst': [], 'aht': []} -->initially empty list for each key
        for each_word in string_list:
            key = ''.join(sorted(each_word))
            #sorted(cat)=act, sorted(act)=act, sorted(pots)=opst, sorted(tops)=opst, sorted(stop)=opst, sorted(hat)=aht
            mapping_dict[key].append(each_word)
            #mapping_dict[act] = [cat, act] 
            #append is joining the *values*[cat,act] to the key[act] in the mapping_dict
            # list(mappinng_dict.keys()) = [act, opst, aht] 
        return list(mapping_dict.values())
                #list(mapping_dict.values()) = [[cat, act], [pots, tops, stop], [hat]]

"""
---without using defaultdict---:-
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in res:
                res[key] = [] #defaultdict is not used here, so we need to check if the key exists in the dictionary. If it doesn't, we initialize it with an empty list.
            res[key].append(s)
        return list(res.values())
"""