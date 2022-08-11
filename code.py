def sums(a,b):
  c = a + b
  return c
x = int(input("x = "))
y = int(input("y = "))
print(sums(x,y))

#to find the smallest number

def list_min(l):
  mini = l[0]
  for i in range(len(l)):
    if (l[i] < mini):
      mini = l[i]
  return mini

#to find the largest number

def list_max(l):
  maxi = l[0]
  for i in range(len):
    if(l[i] > maxi):
      maxi = l[i]
  return maxi

#to append list before given list

def append_before(l,x):
  newl = []
  for i in range(len(x)):
    newl.append(x[i])
  for i in range(len(l)):
    newl.append(l[i])
  return newl

#to append a list after given list

def append_after(l,x):
  newlist = []
  for i in range(len(l)):
    newlist.append(l[i])
  for i in range(len(x)):
    newlist.append(x[i])
  return newlist

#to find out average

def average(l):
  sum = 0
  for i in range(len(l)):
    sum = sum + l[i]
  average = sum/len(l)
return average
