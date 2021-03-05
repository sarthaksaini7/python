word = input()
underscore = "_"
if word.islower() or word.isupper() and "_" not in word:
   word = word.capitalize()
if "_" in word:
    word_list = []
    for i in word:
        word_list.append(i)

    for i in word_list:
        if underscore in word_list:
            word_list.remove("_")
    word = ''.join(word_list)
    word.capitalize()
print(word)