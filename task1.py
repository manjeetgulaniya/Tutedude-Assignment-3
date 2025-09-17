def factorial(a):
    counter=1
    sum=1
    while counter <=a:
        sum=sum*counter
        counter = counter + 1
    print(sum)

num=int(input("Enter the number:\t"))

factorial(num)
    



        