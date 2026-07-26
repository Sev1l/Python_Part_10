## Access modifiers
# Task 2 (Secret magic potion)


class MagicPotion:
    def __init__(self):
        self.list1 = []
        self.list2 = []
    def add_ingredient(self,ingredient,amount):
        self.ingredient = ingredient
        self.amount = amount
        self.list1 += [self.ingredient]
        self.list2 += [self.amount]
        
    def print_recipe(self):
        for i in range(len(self.list1)):
            print(f'{self.list1[i]} {self.list2[i]} grams')
    

class SecretMagicPotion(MagicPotion):
    def __init__(self,name,password):
        super().__init__()
        self.name = name
        self.password = password
        
    def add_ingredient(self,ingredient,amount,password):
        if self.password != password:
            print("ValueError: Wrong password!")
        else:
            super().add_ingredient(ingredient,amount)

    def print_recipe(self,password):
        if self.password != password:
            print("ValueError: Wrong password!")
        else:
            print(f'{self.name}')
            super().print_recipe()


diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
diminuendo.print_recipe("hocuspocus")

diminuendo.print_recipe("pocushocus") # WRONG password!
