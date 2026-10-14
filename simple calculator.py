a=int(input("enter a value"))
b=int(input("enter ab value"))
operator=input("enter the symbol:")
match operator:
  case"+":
    print(a+b)
  case"-":
    print(a-b)
  case"*":
    print(a*b)
  case"/":
    print(a/b)
  case"//":
    print(a//b)
  case"**":
    print(a**b)
  case"%":
    print(a%b)
  case _:
    print("give valid operator")
