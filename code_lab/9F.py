import array

def are_multiples(arr1, arr2, column):
  is_multiple = True
  i=0
  k=0.00
  if arr1 == arr2 :
    return True
  while(i<column) :
    if arr1[i] == 0 or arr2[i] == 0 :
      i+=1
      continue
    else :
      k = arr1[i]/arr2[i]
      break
  if k==0:
    return False
  while(i<column) :
    if arr1[i] == 0 or arr2[i] == 0 :
      if arr1[i] != arr2[i] :
        is_multiple = False
        break
      i+=1
      continue
    if arr1[i]/arr2[i] == k :
      i+=1
      continue
    else :
      is_multiple = False
      break
  return is_multiple

cin = list(map(int, input().split()))
row = cin[0]
column = cin[1]

i=0
kaboom =[]
while(i<row):
  newrow = list(map(int, input().split()))
  kaboom.append(newrow)
  i+=1

answer=[]
i=0
while(i<row):
  j=i+1
  while(j<row):
    if are_multiples(kaboom[i], kaboom[j], column):
      answer.append(str(i+1))
      answer.append(" ")
      answer.append(str(j+1))
      answer.append("\n")
    j+=1
  i+=1

output = ""
for each in answer:
  output+=each
print(output)