result = {}
with open("input.txt", "r", encoding="utf-8") as newFile:
    words = [0]
    while len(words) != 0:
        words = newFile.readline().strip().split()
        for word in words:
            print(result.get(word, 0), end=" ")
            result[word] = result.get(word, 0) + 1

# Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных подряд идущих символов.
# Слова разделены одним или большим числом пробелов или символами конца строки.
# Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось
# в этом тексте ранее
#
# Тест 1
# Входные данные:
# one two one tho three
#
#
# Вывод программы:
# 0 0 1 0 0
