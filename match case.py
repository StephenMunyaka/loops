name = input("what's your name? "))
match name:
    case "jane":
      print("successful") 
    case "june":
       print("successful") 
    case "ken":
       print("successful")
    case _:
    print("unsuccessful")