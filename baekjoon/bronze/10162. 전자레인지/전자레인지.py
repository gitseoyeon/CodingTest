n = int(input()) /
button = [300, 60, 10] 
click = [0, 0, 0]

for i in range(len(button)) :
    if (n >= button[i]):
        click[i] = n // button[i]
        n %= button[i]

if(n > 0):
    print(-1)
else:
    print(click[0], click[1], click[2])