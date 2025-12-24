
pss = "Secret1234"
attempt = 0
max_a = 3

while attempt < max_a:
    attempt += 1
    entr = input("Enter Your Password ")
    if entr == pss:
        print("Welcome batman")
        if attempt == 1:
            print(f"you entered your password in {attempt} Try!!! Welldone")
        else:
            print(f"your total attempts are {attempt}")
        break
    elif attempt < max_a:
        remaining = max_a - attempt
        print(f"Your password is incorrect \n you have {remaining} attempts Left")
    else:
        print("Your Access has been revoked")       

print("End of Program")