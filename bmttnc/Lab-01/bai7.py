print("Mời nhập: (nhập end = kết thúc)")
lines = []
while True:
    line = input()
    if line.lower() == "end":
        break
    lines.append(line)
print("Kết quả")
for line in lines:
    print(line.upper())