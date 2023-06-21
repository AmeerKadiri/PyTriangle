start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
count_by = int(input("Enter the count increment: "))

for num in range(start, end + 1, count_by):
    print(num)