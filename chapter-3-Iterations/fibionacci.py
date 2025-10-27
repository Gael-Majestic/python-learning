def fibionacci(n):
    current, next = 0, 1
    for i in range(n):
        current, next = next, current + next
    return current

x = fibionacci(7)
print(x)