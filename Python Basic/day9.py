# # # #DICTIONARY
# # # #SYNTAX: {Key: Value}
# # # # Elements are identified by keys

# # programming_dictionary = {
# #     "Bug" : "An error which prevent expected output",
# #     "Function": "A piece of code that can be called over and over",
# #    # "Loop":"The action of doing something over and over",
# # }

# # # print(programming_dictionary)

# # # Add new items to dictonary
# # programming_dictionary["Loop"] = "The action of doing something over and over"
# # print(programming_dictionary)

# # # empty_dictonary = {}

# # # # wipe an existing dictonary

# # # # programming_dictionary = {}
# # # # print(programming_dictionary)

# # # # Edit an item in dictionary

# # # (programming_dictionary["Bug"]) = "A moth in your computer"
# # # print(programming_dictionary)

# # # Loop through a dictionary

# # for key in programming_dictionary:
# #     print(key)
# #     print(programming_dictionary[key])

# # ******************************************************XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX****************************************************
# student_scores = {
#   "Harry":100 ,
#   "Ron": 100,
#   "Hermione": 100, 
#   "Draco": 20,
#   "Neville": 100,
# }

# print(student_scores)

# student_grades = {}

# for student in student_scores:
#     if student_scores[student] >= 91 and student_scores[student] <= 100:
#         student_grades[student] = "Outstanding"
#     elif student_scores[student] >= 81 and student_scores[student] <= 90:
#         student_grades[student] = "Excedds expectations"
#     elif student_scores[student] >= 71 and student_scores[student] <= 80:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"


# print(student_grades)
# # ***************************************XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX******************************************


# # NESTING

# # Nesting list in dictionary
# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# #  Nesting Dictionaries in a dictionary

# travel_log = {
    
#         "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12},
#         "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "totoal_visits": 18}
# }

# # Nestinf dictionary in List

# travel_log = [
    
#         {
#             "country": "France", 
#             "cities_visited" : ["Paris", "Lille", "Dijon"],
#             "total_visits": 12
#         },

#         {
#             "country": "Germany",
#             "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
#             "totoal_visits": 18
#         },
# ]


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},

{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},

]
 
country = input("Enter the name of country visited: ")
visits = int(input( " number of visits:  "))
cities = input(" Enter the cities you visited").split( )


def add_new_country( country_name, visits_number, cities_list):
    new_country = {
        "country": country_name,
        "visits": visits_number,
        "cities": cities_list
    }

    travel_log.append(new_country)

add_new_country(country_name= country, visits_number= visits, cities_list= cities)
print(travel_log)



    
    

    