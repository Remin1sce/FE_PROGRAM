import array
row = int(input())
column = int(input())

i=0
kaboom =[]
while(i<row):
  newrow = str(input())
  newlist =[]
  for letter in newrow:
    newlist.append(letter)
  kaboom.append(newlist)
  i+=1

answer=[]
i=0
while(i<row):
  j=0
  newline = []
  while(j<column):
    count=0
    if kaboom[i][j] == '*' :
      newline.append('*')
      j+=1
      continue
    #check topleft
    if i!=0 and j!=0 :
      if kaboom[i-1][j-1] == '*' :
        count+=1
    #check topmiddle
    if i!=0:
      if kaboom[i-1][j] == '*':
        count+=1
    #check topright
    if i!=0 and j!=column-1 :
      if kaboom[i-1][j+1] == '*' :
        count+=1
    #check middleleft
    if j!=0 :
      if kaboom[i][j-1] == '*' :
        count+=1
    #check middleright
    if j!=column-1 :
      if kaboom[i][j+1] == '*' :
        count+=1
    #checklowerleft
    if i!=row-1 and j!=0 :
      if kaboom[i+1][j-1] == '*' :
        count+=1
    #checklowermiddle
    if i!=row-1 :
      if kaboom[i+1][j] == '*':
        count+=1
    #checklowerright
    if i!=row-1 and j!=column-1:
      if kaboom[i+1][j+1] == '*':
        count+=1
    newline.append(str(count))
    j+=1
  answer.append(newline)
  i+=1

output=""
for rowcount in answer:
  for columncount in rowcount:
    output+=columncount
  output+="\n"

print(output)