class a:
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")
class b(a):
    def feature3(self):
        print("feature 3 working")
    def feature3(self):
        print("feature 4 working")

a1 = a()

a2=b()
a2.feature1()