def groupAnagrams(strs):
    anagrams = {}

    for str in strs:
        sorted_s = ''.join(sorted(str))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(str)
        else:
            anagrams[sorted_s] = [str]
        print(anagrams)

    return  list(anagrams.values())
    # for s in strs:
    #     sorted_s = ''.join(sorted(s))
    #     if sorted_s in anagrams:
    #         anagrams[sorted_s].append(s)
    #     else:
    #         anagrams[sorted_s] = [s]
    # return list(anagrams.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))  # Output: [["eat","tea","ate"],["tan","nat"],["bat"]]