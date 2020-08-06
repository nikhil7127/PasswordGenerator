def check(string):
  check=[]
  all_check =[]
  for a in string:
    check.append(a.islower())
    if(len(check)==len(string)):
      all_check.append(any(check))
      check =[]
      for a in string:
        check.append(a.isupper())
        if(len(check)==len(string)):
          all_check.append(any(check))
          check =[]
          for a in string:
            check.append(a.isdigit())
            if (len(check)==len(string)):
              all_check.append(any(check))
  if(all(all_check) and len(string) >=8):
      #print("strong password")
      return True
  else:
      #print("please change password")
      return False
if __name__ == "__main__":
  if (check("nikhildg")):
    print("hello")
  else:
    print("pass")

