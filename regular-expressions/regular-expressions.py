import re

five_digit_zip = '98101'
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'
five_digit_expression = r'\d{5}'
nine_digit_expression = r'\d{5}-\d{4}'
phone_number_expression = r'\d{3}-\d{3}-\d{4}'
print(re.search(five_digit_expression, five_digit_zip ))
print(re.search(nine_digit_expression, nine_digit_zip ))
print(re.search(phone_number_expression, phone_number ))

my_phone = '010 4545-345'
my_phone_expression = r'^\d{3}\s\d{4}-\d{3}$'  
print(re.search(my_phone_expression, my_phone))

# all regular expression will be here : https://www.debuggex.com/cheatsheet/regex/python
# and this website for test ur regular expressions : https://regex101.com/