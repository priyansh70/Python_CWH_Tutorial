marks = (['30,','56,','89\n'],['43,','24,','74\n'],['34,','75,','72\n'])

# WriteLines
f = open('marks.txt','w')
for mark in marks:
    for m in mark:
        f.writelines(m)
f.close()    


# ReadLines 
f = open("marks.txt",'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is: {m1*2}")
  print(f"Marks of student {i} in English is: {m2*2}")
  print(f"Marks of student {i} in SST is: {m3*2}")
  print()