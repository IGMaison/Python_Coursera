result = {}
with open("input.txt", "r", encoding="utf-8") as newFile:
    word = "0"
    sumVote = 0
    while len(word) != 0:
        word = newFile.readline().strip()
        if len(word) != 0:
            result[word] = result.get(word, 0) + 1
            sumVote += 1
first = (sorted(result.items(), key=lambda d: d[1], reverse=True))[0][0]
with open("output.txt", "w", encoding="utf-8") as newFile:
    if int(result[first]) * 2 > sumVote:
        print(first, file=newFile)
    else:
        print(first, file=newFile)
        print((sorted(result.items(), key=lambda d: d[1],
                      reverse=True))[1][0], file=newFile)

# В выборах Президента Российской Федерации побеждает кандидат, набравший свыше
# половины числа голосов избирателей. Если такого кандидата нет, то во второй
# тур выборов выходят два кандидата, набравших наибольшее число голосов.
#
# Формат ввода
#
# Каждая строка входного файла содержит имя кандидата, за которого отдал голос
# один избиратель. Известно, что общее число кандидатов не превосходит 20, но
# в отличии от предыдущих задач список кандидатов явно не задан. Читайте данные
# из файла input.txt с указанием кодировки utf8.
#
# Формат вывода
#
# Если есть кандидат, набравший более 50% голосов, программа должна вывести его
# имя. Если такого кандидата нет, программа должна вывести имя кандидата,
# занявшего первое место, затем имя кандидата, занявшего второе место. Выводите
# данные в файл output.txt с указанием кодировки utf8.
