def find_max_repeated_word(f):
    with open(f,'r') as fr:
        lines = fr.readlines()
    print(lines)

    d={}
    for line in lines:
        raw = line.split()
        # print(raw)

        for element in raw:
            if element in d:
                d[element]+=1
            else:
                d[element] = 1
    # print(d)

    count = 0

    for element in sorted(d.items(), key=lambda x: x[1], reverse=True) :
        count= count +1
        if count==10:
            break
        print(element)
from collections import Counter
def find_max_repeated_word_2(f):
    with open(f,'r') as fr:
        lines = fr.read()
    line= lines.split()
    print(line)
    count= Counter(line)
    # print(count)
    print(count.most_common(1)[0])


import  pandas as pd
from collections import Counter

import pandas as pd
from collections import Counter


def find_max_repeated_word_pandas(f):
    # Read the file using pandas
    df = pd.read_csv(f, header=None, names=['text'])

    # Split the text into words
    words = df['text'].str.split(expand=True).stack()

    # Use Counter to count word frequencies
    word_counts = Counter(words)

    # Get the most common word
    most_common_word = word_counts.most_common(1)[0]

    return most_common_word




f="/Users/vishnoiprem/PycharmProjects/data.code.cloud/data/find_max_repeated_word.csv"

print(find_max_repeated_word(f))
print(find_max_repeated_word_2(f))
print(find_max_repeated_word_pandas(f))