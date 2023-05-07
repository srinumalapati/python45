phrase=input("input words: ")
phrase_list=phrase.split(",")
phrase_list.sort()
print((',').join(phrase_list))