def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if(n % i == 0):
            return False
    return True
print("Nhap n: ")
n = int(input())
if(is_prime(n)):
    print(n, "la so nguyen to")
else:
    print(n, "khong phai la so nguyen to")