emotion_wordsfile = open("emotion_words.txt", "r")
num_lines = 0

for aline in emotion_wordsfile:

    values = aline.split(",")
    num_lines += 1
    print(num_lines)
    # print(values[0], "is from", values[3], "and is on the roster for", values[3])

emotion_wordsfile.close()
