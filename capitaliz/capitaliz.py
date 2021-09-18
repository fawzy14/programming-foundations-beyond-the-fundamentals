# capitaliz the name 
first_name = 'mahmoud'
last_name = 'fawzy'
note = 'award: Nople Peace Prize'
first_name_cap = first_name.capitalize()
last_name_cap = last_name.capitalize()
print(first_name_cap)
print(last_name_cap)

# Look for string using .find
award_location = note.find('award: ')  #award
                                       #01234 
print(award_location) #the result will be 0 
#or 
award_text = note[7:]   # 7 bc we need to show the Nople ...... and 7 is the beginning of this text 
print(award_text) 

#or 
text = note[0:5] #the result will be 'award' only 
print(text)                          #012345 