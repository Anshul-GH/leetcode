class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_numbers = []
        output = []

        for string in strs:
            str_num = [ord(chr) for chr in string]
            str_num.sort()
            strs_numbers.append(tuple(str_num))
        
        strs_dict = {}
        for idx, val in enumerate(strs_numbers):
            if val in strs_dict:
                strs_dict[val].append(idx)
            else:
                strs_dict[val] = [idx]

        for value in strs_dict.values():
            anagrams = [strs[i] for i in value]
            output.append(anagrams)

        return output
