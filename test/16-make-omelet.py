#!/usr/bin/python

class Fridge:

    def __init__(self, items={}):

        if type(items) != type({}):
            raise TypeError("Fridge requires a dictionary but was given %s" % type(items))
        self.items = items
        return


    def __add_multi(self, food_name, quantity):

        if (not food_name in self.items):
            self.items[food_name] = 0
        self.items[food_name] = self.items[food_name] + quantity


    def add_one(self, food_name):

        if type(food_name) != type(""):
            raise TypeError, "add_one requires a string, given a %s" % type(food_name)
        else:
            self.__add_multi(food_name, 1)
        return True

    def add_many(self, food_dict):

        if type(food_dict) != type({}):
            raise TypeError("add_many requires a dictionary, got a %s" % food_dict)
        for item in food_dict.keys():
            self.__add_multi(item, food_dict[item])
        return

    """
    >>> f = Fridge({"eggs":6, "milk":4, "cheese":3})
    >>> f.items
    {'cheese': 3, 'eggs': 6, 'milk': 4}
    >>> f.add_one("grape")
    True
    >>> f.items
    {'cheese': 3, 'eggs': 6, 'grape': 1, 'milk': 4}
    >>> f.add_many({"mushroom":5, "tomato":3})
    >>> f.items
    {'tomato': 3, 'cheese': 3, 'grape': 1, 'mushroom': 5, 'eggs': 6, 'milk': 4}
    """ 

    def has(self, food_name, quantity=1):

        return self.has_various({food_name:quantity})


    def has_various(self, foods):

        try:
            for food in foods.keys():
                if self.items[food] < foods[food]:
                    return False
            return True
        except KeyError:
            return False

    """
    >>> f= Fridge({"eggs":6, "milk":4, "cheese":3})
    >>> if f.has("cheese", 2):
    ...     print("It's time to make an omelet!")
    ... 
    It's time to make an omelet!
    """

    def __get_multi(self, food_name, quantity):

        try:
            if (self.items[food_name] is None):
                return False;
            if (quantity > self.items[food_name]):
                return False;
            self.items[food_name] = self.items[food_name] - quantity
        except KeyError:
            return False
        return quantity


    def get_one(self, food_name):

        if type(food_name) != type(""):
            raise TypeError("get_one requires a string, given a %s" %type(food_name))
        else:
           result = self.__get_multi(food_name, 1)
        return result


    def get_many(self, food_dict):

        if self.has_various(food_dict):
            foods_removed = {}
            for item in food_dict.keys():
                foodds_removed[item] = self.__get_multi(item, food_dict[item])
            return foods_removed


    def get_ingredients(self, food):

        try:
            ingredients = self.get_many(food.__ingredients__())
        except AttributeError:
            return False
        if ingredients != False:
            return ingredients



