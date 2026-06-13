text = input()
ch = input()
if ch in text:
    print(text.find(ch)-1)
else:
    print(-1)