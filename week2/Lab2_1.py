num = int(input("Enter a number: ") )
if num < 0:
    text = f"{num} is negative"
    if num == 0 or num % 2 == 0:
        print(text,"and even")
    else:
        print(text,"and odd")
elif num > 0:
    text = f"{num} is positive"
    if num == 0 or num % 2 == 0:
        print(text,"and even")
    else:
        print(text,"and odd")
else:
    text = f"{num} is zero"
    print(text)