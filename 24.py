a = int(input())
b = int(input())
print("YES" * (-(a % b) + 1) + "NO" * (-(-(a % b) // b)))
