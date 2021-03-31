from string import punctuation as punct

spam = []

# remove spam
for sentence in open('data.csv', 'r', encoding='utf8'):
    sentence = ''.join([char for char in sentence if char not in punct])
    for word in sentence.split():
        # check if word is just digits
        if not word.isdigit():
            for char in word:
                if char.isdigit():
                    spam.append(sentence)
                    break

# non spam
with open('result.csv', 'w', encoding='utf') as f:
    for sentence in open('data.csv', 'r', encoding='utf8'):
        new_sentence = ''.join([char for char in sentence if char not in punct])
        if new_sentence not in spam:
            f.write(sentence)
