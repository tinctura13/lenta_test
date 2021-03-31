import sys
from string import punctuation as punct

input_file = sys.argv[0]


def primitive_spam_filter():
    """
    Primitive script that works on heuristics and pretend to filter spam
    messages from the mail. Spam messages considered as words with integers
    inside them.

        :return: It saves all messages identified as not spam to 'result.csv'
    """
    spam = []

    # define spam
    for sentence in open(input_file, 'r', encoding='utf8'):
        sentence = ''.join([char for char in sentence if char not in punct])
        for word in sentence.split():
            # check if word is just digits
            if not word.isdigit():
                for char in word:
                    if char.isdigit():
                        spam.append(sentence)
                        break

    # select non spam
    with open('result.csv', 'w', encoding='utf') as f:
        for sentence in open('data.csv', 'r', encoding='utf8'):
            new_sentence = ''.join([char for char in sentence if char not in punct])
            if new_sentence not in spam:
                f.write(sentence)