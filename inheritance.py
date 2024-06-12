class animal :
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    
    def printname(self):
        print(self.name,self.breed)

class cat(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,breed)
        self.sound="MEOW"
    
    def printname(self):
        print(self.name,self.breed,self.sound)
        
x = animal("Dog","retriever")
x.printname()
c = cat("punchi","ragdoll")
c.printname()