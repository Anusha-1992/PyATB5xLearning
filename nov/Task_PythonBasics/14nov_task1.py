n1 =int(input("Enter the length side 1: "))
n2 =int(input("Enter the length side 2: "))
n3 =int(input("Enter the length side 3: "))

if n1 == n2 and n1==n3 and n2==n3:
    print(" Triangle is  equilateral")
elif n1 == n2 and n2 < n3 :
    print(" Triangle is  isosceles")
else:
    print("Triangle is scalene")
