def findSubstrings(string):
    ms = string
    substrings = []
    for i in range(len(ms)):
        for j in range(i+1,len(ms)+1):
            substrings.append(ms[i:j])
    return substrings
