def check_fermat(a, b, c, n):

    if n < 2:
        print("n needs to be 2 or greater to check Fermat's last theorem. Duh!")
    else:
        if (a ** n + b ** n) == (c ** n):
            print("Whaddaya know, Fermat was wrong?")
        else:
            print("No, that doesn't work. So far Fermat is on the money.")

def user_check():
    
    a = int(input("Give me a value for a: "))
    b = int(input("Give me a value for b: "))
    c = int(input("Give me a value for c: "))
    n = int(input("Give me a value for n: "))

    check_fermat(a, b, c, n)

user_check()