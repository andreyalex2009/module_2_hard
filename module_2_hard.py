def generate_password(n):
    password = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                password.append((str(i), str(j)))
    return ''.join(map(''.join, password))
for num in range(3, 21):
    print(num, '->', generate_password(num))