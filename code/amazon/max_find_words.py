def find_max_repeated_word(f):
    with open(f,'r') as f:
        lines = f.read()
    list_line = lines.split()
    d ={}
    for raw in list_line:
        if raw in d:
            d[raw]+=1
        else:
            d[raw]=1

    for element in sorted(d.items(), key=lambda x: x[1], reverse=True):
        print(element)
        break


f="/Users/vishnoiprem/PycharmProjects/data.code.cloud/data/find_max_repeated_word.csv"
print(find_max_repeated_word(f))
#