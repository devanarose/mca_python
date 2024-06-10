# class mca_sem : 
#     name = "revathi"
#     namee = "merin and gracen"
#     def duties(self) :
#         self.d = "track placement status"
#         print(self.d)

# class_rep = mca_sem()
# print("class rep : ",class_rep.name)
# placement_rep = mca_sem()
# print("placement rep : ",placement_rep.namee)
# placement_rep.duties()


class mca_sem3 :
    def __init__(self,classrep1,classrep2):
        self.name1 = classrep1
        self.name2 = classrep2
    def func1(self):
        print("ClassRep 1: " + self.name1 + "\nClassrep 2: " + self.name2)
    def duties(self) :
         self.d = "track placement status"
         print(self.d)

mca = mca_sem3("SIVANAND","REVATHI")
mca.func1()
mca.duties()