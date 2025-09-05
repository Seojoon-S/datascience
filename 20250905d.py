import matplotlib.pyplot as plt
f = open("Alice.txt", "r", encoding = "utf-8")
book = f.read()
words = input("검색하려고 하는 단어를 5개 입력해 주세요 : ")
words = words.split()
cnt = []
for word in words :
    n = book.count(word)
    cnt.append(n)
f.close()
plt.rc("font", family = "Malgun Gothic")
plt.title("단어 검색 결과")
plt.xlabel("검색 단어")
plt.ylabel("단어 개수")
plt.bar(words, cnt)
plt.show()
