# # dictionary is a data structure that allows us to store datas as key - value format.
# # In dictionary we can store data as key value pairs. key is the index of its value in dictionary.

# names = {
#     "Ripon" : "Singha",
#     "Rishav" : "sardar",
#     "Deep" : "Debnath",
#     "Rajasmita" : "mitra",
# }
# # this is a simple example of dictionarie keys as where there at the right left side as the index for iteration and the values are at the right side


# # using loop to print the dictionary keys.
# for name in names:
#     print(name)
# # it will print the keys of that dictionary not the values in it


# # it will give the values of these keys
# print(names["Ripon"])
# print(names["Rishav"])
# print(names["Rajasmita"])


# #printing both keys are values using loop
# for name in names:
#     print(name, names[name])



# when we need to store multiple datas into a dictionary but it get so messy over time so we use the list of dictionary
# a list of dictionary is a list of multiple dictionaries in one single list
students = [
    {"name" : "Hermoione", "House" : "Gryffindor", "Patronous" : "Otter"},
    {"name" : "Harry", "House" : "Gryffindor", "Patronous" : "Stag"},
    {"name" : "Ron", "House" : "Gryffindor", "Patronous": "Jack Russle terrier"},
    {"name" : "Dreco", "House": "Slytherin", "Patronous" : None}
]
# this is a list of dictionaries where [] indicates the list and {} indicates the dictionaries.

# printing the values of those dictionaries using loop
for student in students:
    print(student["name"], student["House"], student["Patronous"], sep = ", ")


# printing the key and values both of those dictionaries using nested for loop and by using item() function that extracting each key and value pairs and assigning them to "key" and "value" variable in inner loop
for student in students:
    for key, value in student.items():
        print(f"{key}: {value}", end=", ")
    print() 