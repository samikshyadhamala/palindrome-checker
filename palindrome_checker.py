#to check if the given string is palindrome or not
st=input("enter a word=")
if st.isalnum()==True:
  rev_str=st[::-1]

  if st==rev_str:
    print(f'{st} is palindrome.')
    
  else:
    print(f'{st} is not a plindrome.')

else:
    print("only number and words are valid and no space allowed")