class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")
    def make_salad(self):
        print("The chef makes a salad")
    def make_special_dish(self):
        print("The chef makes bbq rips")

# from Chef import Chef
class ChineseChef(Chef):
    def make_special_dish(self):
        print("The chef makes orange chicken")
    def make_rice(self):
        print("The chef makes rice")

# from Chef import Chef
# from ChineseChef import ChineseChef
myChef = Chef()
myChef.make_chicken()

myCC = ChineseChef()
myCC.make_chicken()
myCC.make_special_dish()