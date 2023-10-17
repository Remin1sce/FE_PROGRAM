a = []
while True:
  b = input()
  if b == "$":
    break
  else:
      a.append(b)
def find_longest_word(a):
    longest_word = max(a, key=len)
    return longest_word
def find_shortest_word(a):
    shortest_word = min(a, key=len)
    return shortest_word
shortest_word =  find_shortest_word(a)
longest_word = find_longest_word(a)
print(shortest_word)
print(longest_word)