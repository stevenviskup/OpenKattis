# take input.split
x,dominant = input().split()
x = int(x)
points = 0
#4 cards per hand
for i in range (4*x):
  card = input()

  if card[-1] == dominant:
    if card[0] == "A":
      points += 11
    elif card[0] == "K":
      points += 4
    elif card[0] == "Q":
      points += 3
    elif card[0] == "J":
      points += 20
    elif card [0] == "T":
      points += 10
    elif card [0] == "9":
      points += 14
    else:
      pass 
    
  if card[-1] != dominant:
    if card[0] == "A":
      points += 11
    elif card[0] == "K":
      points += 4
    elif card[0] == "Q":
      points += 3
    elif card[0] == "J":
      points += 2
    elif card [0] == "T":
      points += 10
    elif card [0] == "9":
      points += 0
    else:
      pass  


#print points
print(points)