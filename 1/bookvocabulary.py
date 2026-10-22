book1 = "python is easy and useful"
book2 = "python is powerful and useful"

words1 = set(book1.lower().split())
words2 = set(book2.lower().split())

print("Book 1 Unique Words:", words1)
print("Book 2 Unique Words:", words2)
print("Common Words:", words1.intersection(words2))
print("Words only in Book 1:", words1.difference(words2))
print("Words only in Book 2:", words2.difference(words1))
print("Total Unique Words:", len(words1.union(words2)))