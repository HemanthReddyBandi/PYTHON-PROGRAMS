a=input('name:')
b=input('name:')
a_sort=sorted(a)
b_sort=sorted(b)
anagram=a_sort==b_sort
if anagram:
    print(a,"is anagram")
else:
    print(b,"is not anagramhep")