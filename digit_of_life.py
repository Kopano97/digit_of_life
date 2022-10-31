
dob = input("Enter your date of birth: ")


while True:
    num = 0
    for s in dob:
        num = num + int(s)
    
    if len(str(num)) == 1:
        print(num)
        break
    else:
        dob = str(num)
        print(dob)
        continue
