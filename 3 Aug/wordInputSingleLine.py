inp = input("Enter your String : ")
words_list=inp.split()

res = [word for word in words_list if len(word)>=2 and word[0] == word[-1]]

print(res)