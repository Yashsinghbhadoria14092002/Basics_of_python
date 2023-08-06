a = {}            # empty dictionary
# print(a, type(a))
b = set()         # empty set
# print(b, type(b))

dict1 = {"good": "Something pleasant", "fetch": "to bring", "1": "The number 1"}
print(dict1["good"])

marks = {"Harshit": 34, "Harry": 99, "Shivani": 8, "Smriti": 45, "Naina": 87, "Sankalp": 78}
print(marks["Harry"])

marks["Priyanka"] = 34
print(marks)

print(marks.get("Priyanka Chopra"))     # this will give none as no key of this name exists
# print(marks["Priyanka Chopra"])         # this will give error as no key of this name exists
print(marks.get("Priyanka"))
print(marks["Priyanka"])

print(marks.keys())
print(marks.values())
print(marks.items())