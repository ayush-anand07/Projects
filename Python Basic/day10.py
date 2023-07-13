#  # FUNCTION WITH OUTPUTS

# def my_function():
#     result = 3*2
#     return 0

# output = my_function() # ----------> This my_function() will be replaced by return result.
# print(output)          #----------->  


def format_name(f_name, l_name):
    """ Take a first name and last name format it to return 
        the title case version of the name""" #Docstrings----> Tells what our function will do. Always put these strings under three double quotes

    a = f_name.title()
    b = l_name.title() 
    return (f'{a} {b}')

print(format_name("ayush", "anand"))   



def is_leap(year):
  """ This function will take year as input and check 
       whether it a leap year or not. return True and False"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
       return True
      else:
        return False
    else:
     return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year):
      if month== 2:
          return 29
  else:
    return month_days[month-1]


  

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

