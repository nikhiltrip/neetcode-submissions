class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        labels = {}
        for word in strs:
            label = "".join(sorted(word))
            if label not in labels:
                labels[label] = []
                labels[label].append(word)
            else:
                labels[label].append(word)
        
        return list(labels.values())
            

 