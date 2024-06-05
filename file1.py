#type of the variable
#a=12.2
#print(type(a))

#str type
#str = 'devana'
#print(type(str))

#concat 2 stings
# firstname = 'Devana '
# lastname = 'Rose Emmanuel'
# print("My name is ",firstname+lastname)

 #sequence type (list)
# l = ['devana','rose','emmanuel']
# print(l)
# number = [1,2,3,4,5]
# print(number)
# print(type(l))
# print(type(number))
# k = list((1.0,2,3,4,5))
# print(k)
# print(type(k))
# listt=[1.0,2,3,4,5,('a','b','c')]
# print(listt)

#dictionary
d={
    'name' : 'Devana',
    'place' : 'kadavanthara',
    'age' : 21,
    'subject' : {
        'maths' : 55,
        'english' :66,
        'computer' : 78
    }
}
print(d['name'])
print(d['subject'])
print(d.get("age"))
#d["subject"]["maths"] = 67
d.get("subject").update({"maths":87})
print(d['subject'])
d.pop("age")
print(d)
