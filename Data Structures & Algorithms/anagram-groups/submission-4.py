class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for word in strs:
            key="".join(sorted(word))
            #act will become a,c,t then act on join
            if key not in dict:
                dict[key]=[] #create key with no value for now
            dict[key].append(word) #along with key append the word value
        return list(dict.values())
            
        
        