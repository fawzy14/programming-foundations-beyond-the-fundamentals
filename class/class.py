class Member(): #class 
                          
    def __init__(self, fname, mname, lname, gender):  #method 
        
        self.fname = fname
        self.mname = mname 
        self.lname = lname 
        self.gender = gender 

    def name_with_title(self):    #method

        if self.gender == 'Male':
         return f'Hello Mr {self.fname}, Nice to meet u.'
        
        elif self.gender == 'Female':
            return f'Hello Mss {self.fname}, Nice to meet u.'
        
        else : 
            return f'Hello {self.fname}, Nice to meet u.'

    def full_name(self):

        return f'{self.fname} {self.mname} {self.lname}'
    

    def all_info(self):

        return f'{self.name_with_title()} and ur full name is : {self.full_name()}'            

member_one = Member('Mahmoud', 'Fawzy', 'Mostafa', 'Male')
member_two = Member('Mohamed', 'Ehab', 'Salma', 'Male')
member_three = Member('Mariam', 'Ahmed', 'Ebrahim', 'Female')
member_four =  Member('Salma', 'Mohamed', 'Gamal', 'gender')

print(member_one.fname)            #print member first name 

print(member_one.name_with_title())            #print Mr (gender) 
print(member_three.name_with_title())           #print Mss (grender)

print(member_three.full_name())          #print member full name 

print(member_two.all_info())           #print member's all info 