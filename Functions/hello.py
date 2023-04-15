# //write the item from the following items in that item fromlist 1 is the key
# //and the list 2 isthe value
keys = ["JavaScript","Kotlin","Python"]
values = [60,25,30]
scores_dict=dict(zip(keys,values))
print(scores_dict)
#insights
# zip()=>takes in a multiple collection and return a new collection

#Create a new dictionary by extracting the keys from a given dictionary
#keys to extract are name and hobby and also remove the key of age and county
student_dict = {
    "name":"Emmily Stephanie",
    "Age":20,
    "Occupation":"Student",
    "Hobby":"Football player",
}
keys = ["name","Hobby","Occupation","Age"]
newdict = {k:student_dict[k]for k in keys}
print(newdict)

# #remove
keys = ["Age","Occupation"]
for k in keys:
    student_dict.pop(k)
    print(student_dict)

#check if a vallue exists in a dictionary
detail_dict = {"name":"Emmily","course":"Software Developer"}
if "Software Developer" in detail_dict.values():
    print("It exists")  
#get the the key of a minimum value in the following dictionary
Weight_dict = {
    "Jane":86.90,
    "Emmie":57.95,
    "Faith":65.65,
}
print(min(Weight_dict,key=Weight_dict.get))
print(max(Weight_dict,key=Weight_dict.get))
#Merge two dictionaries into one dictionary
