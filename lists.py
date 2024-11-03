# Lists are mutable sequences, typically used to store collections of homogeneous items
# (where the precise degree of similarity will vary by application).
num_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
num_list = [x for x in num_list if x!=1]
print(num_list)

def find_palindromes(word_list):
        palindromes = [word for word in word_list if word == word[::-1]]
        return palindromes

words = ["level", "python", "radar", "hello"]
result = find_palindromes(words)
print(result)