#Activity 5.2: Word Frequency Counter (using Dictionary)

sentence = input("Please put your sentence : ")
words = sentence.split()
#print(words)
word_counts = {}

for word in words:

    word = word.strip('.,!?"')

    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)