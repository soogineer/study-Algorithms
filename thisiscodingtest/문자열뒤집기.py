s = input()
count0 = 0
count1 = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
      if s[i+1] == '1':
        count0 += 1
      else:
        count1 += 1

print(min(count0, count1))