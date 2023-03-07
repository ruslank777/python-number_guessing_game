from collections import defaultdict

def group_anagrams(words_list):
    dfdict = defaultdict(list)
    for item in words_list:
        # first lets make a keys for the dictionary by sorting letters in each word
        sort_item = " ".join(sorted(item))
        # use this key in dictionary and append the original unsorted word to the value list associated with that key.
        dfdict[sort_item].append(item)
    return dfdict.values()

if __name__ == '__main__':
    words = ["tea", "eat", "bat", "ate", "arc", "car"]
    print(group_anagrams(words))