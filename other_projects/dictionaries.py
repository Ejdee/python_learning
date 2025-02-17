# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# print(programming_dictionary["Bug"])
#
# #adding stg in the dictionary
# programming_dictionary["Loop"] = "Something that is done time after time"
# print(programming_dictionary["Loop"])
#
# #empty dictionary
# empty_dictionary = {}
#
# #loop through dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#nesting dictionaries

# travel_log = {
#     "France": {"cities visited": "Paris, Lyon, Villon", "total_visits": 12},
#     "Germany": {"cities visited": "Hamburg, Berlin, Stalingrad", "total_visits": 3}
# }

# #nesting dictionary in a list
#
# travel_log = [
#     {"country": "France",
#      "cities visited": "Paris, Lyon, Villon",
#      "total_visits": 12
#      },
#     {"county": "Germany",
#      "cities_visited": "Berlin, Hamburg, Frankfurt",
#      "total_visits": 3
#      }
# ]




# #practice
#
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
#
# student_grades = {}
#
#
# for name in student_scores:
#     if student_scores[name] > 90:
#         student_grades[name] = "Outstanding"
#     elif 80 < student_scores[name] <= 90:
#         student_grades[name] = "Exceeds Expectations"
#     elif 70 < student_scores[name] <= 80:
#         student_grades[name] = "Acceptable"
#     else:
#         student_grades[name] = "Fail"
#
# print(student_grades)


#practice 2

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
#🚨 Do NOT change the code above

#to be added to the travel_log. 👇

def add_new_country (country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
