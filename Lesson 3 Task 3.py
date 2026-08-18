## Object oriented programming techniques
# Task 3 (An iterable shopping list)



class ShoppingList:
    def __init__(self):
        self.products = []   

    def add(self, name, quantity):
        self.products.append((name, quantity))

    def __iter__(self):
        self.index = 0       
        return self

    def __next__(self):
        if self.index >= len(self.products):
            raise StopIteration
        product = self.products[self.index]
        self.index += 1
        return product


shopping_list = ShoppingList()
shopping_list.add("bananas", 10)
shopping_list.add("apples", 5)
shopping_list.add("pineapple", 1)

for product in shopping_list:
    print(f"{product[0]}: {product[1]} units")


