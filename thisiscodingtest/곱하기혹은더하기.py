s = input()
answer = 0

for i in range(1, len(s)):
    if (s[i] <= 1 or answer <= 1):
      answer += s[i]
    else:
      answer *= s[i]

print(answer)


