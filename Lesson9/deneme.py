
import string
import re

book=["Merhaba, benim adım Okan. Evet benim ismim Okan Yıldırım. Merhaba Dünya ile başladım kodlamaya.",
      "Merhaba, Okan. Benim ismim de Hilal.",
      "Tanıştığıma memnun oldum."]
word_counts={}
word_list=[]
for line in book:
    data=line.strip().split(" ")
    for word in data:
        word_list.append(word)

for word in word_list:
    word_without_puctiontion =re.sub(r'[^\w\s]','',word).lower()
    word_list[word_list.index(word)]=word_without_puctiontion

for word in word_list:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

print(word_list)
print(word_counts)

