a = ("abba", "bbaa", "abbaba", "bbaabb")
for i in a:
    if i == i[::-1]:
        print(f'"{i}" is a palindrome')
    else:
        print(f'"{i}" is NOT a palindrome')