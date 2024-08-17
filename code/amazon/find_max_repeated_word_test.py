def find_max_repeated_word(f):

    with open(f, 'r') as f:
        line = f.read().split()
    print(line)
    d = {}

    for s in line:
        if s in d:
            d[s] = d[s] + 1
        else:
            d[s] = 1
    return sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0]


from  collections import  Counter
def find_max_repeated_word_count(f):
    with open(f, 'r') as f:
        line = f.read().split()
    count = Counter(line)
    print(count[0])


f="/Users/prem/PycharmProjects/data.code.cloud/data/find_max_repeated_word.csv"

print(find_max_repeated_word(f))
print(find_max_repeated_word_count(f))

