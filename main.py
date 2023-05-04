n = int(input("Сколько строк треугольника Паскаля вывести ? "))
# making a triangle matrix of t
t = [[1]]
for i in range(1,n):
  if i == 1:
    t.append([1,1])
  else:
    newLine = [1]
    for j in range(i-1):
      newLine.append(t[i-1][j] + t[i-1][j+1])
    newLine.append(1)
    t.append(newLine)
print("Triangle Matrix")
for i in range(n):
  print(t[i])
      
# how much digits in the biggest number
nCharLast = max([len(str(x)) for x in t[n-1]])
print("Output summed numbers under:")
for i in range(len(t)):
  indent = ("{:{align}{width}s}".format(" ",align = "^",width=(nCharLast-1))*((len(t)-i)))
  print(indent,end="")
  for j in range(len(t[i])):
    num = "{:{align}{width}d}"
    print(num.format(t[i][j],align="^",width=(nCharLast+1)),sep="",end="")
  print()    
