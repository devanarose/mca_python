# class animal :
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed
    
#     def printname(self):
#         print(self.name,self.breed)

# class cat(animal):
#     def __init__(self,name,breed):
#         super().__init__(name,breed)
#         self.sound="MEOW"
    
#     def printname(self):
#         print(self.name,self.breed,self.sound)
        
# x = animal("Dog","retriever")
# x.printname()
# c = cat("punchi","ragdoll")
# c.printname()

#polymorphism

class cat :
    def printt(self):
        print("meow")
class dog :
    def printt(self):
        print("bark")
class cow :
    def printt(self):
        print("moooo")

cat().printt()
dog().printt()
cow().printt()

    
import datetime
x = datetime.datetime.now()
print(x)