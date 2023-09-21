import requests
import random
from collections import Counter

# importing words from a website link
word_dictionary_site_url = 'https://www.mit.edu/~ecprice/wordlist.10000'
response =  requests.get(word_dictionary_site_url)
words = response.content.splitlines()

#-----------------------------------------------------------------------------------
# Displaying the wor
choice = random.choice(words)
choice = str(choice.decode())
print(choice)
results = []
length = len(choice)
choice = choice.lower()
for i in range(0,length):
    results.append('_')
    print('_ ' , end = '')

#------------------------------------------------------------------------------------
count = 0
C = Counter(choice)
nr = 0
while count < 6 and nr != length:
    word = input("Please input your guess: ")
    word = word.lower() 
    if C[word]  == 0 :
        count += 1
    elif C[word] > 0:
        for i in range(0,length):
            if choice[i] == word:
                if results[i] == '_':
                    results[i] = word
                    C[word] -= 1
                    nr += 1
                    print(results)
                    break
                else:
                    continue


