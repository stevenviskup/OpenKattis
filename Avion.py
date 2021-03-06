rows = []

for i in range(5):
  x = input()
  if "FBI" in x:
    rows.append(i+1)

if len(rows) == 0:
  print("HE GOT AWAY!")
else:
  print(' '.join(map(str,rows)))