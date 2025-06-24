def count_word_frequencies(datamap):
    word_count = {}
    with open(datamap, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                word = word.strip('.,!?()[]{}"\'')
                if word:
                    word_count[word] = word_count.get(word, 0) + 1
    return word_count

filename = 'datamap.txt'
frequencies = count_word_frequencies(filename)

count = 0
for word, freq in frequencies.items():
    print(f"{word}: {freq}", end='  ')
    count += 1
    if count % 5 == 0:
        print()  

