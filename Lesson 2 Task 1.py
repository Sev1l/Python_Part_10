## Access modifiers
# Task 1 (Supergroup)


class SuperHero:
    def __init__(self,name,types):
        self.name = name
        self.types = types


class SuperGroup:
    def __init__(self,name,location):
        self._name = name
        self._location = location
        self._members = []

    def get_name(self):
        return self._name
    def get_location(self):
        return self._location

    def add_member(self,hero: SuperHero):
        self._members += [hero]

    def print_group(self):
        print (f'{self._name}, {self._location} \nMembers:')
        for hero in self._members:
            print(f'{hero.name}, superpowers: {hero.types}')
         



superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
invisible = SuperHero("Invisible Inca", "Invisibility")
revengers = SuperGroup("Revengers", "Emerald City")

revengers.add_member(superperson)
revengers.add_member(invisible)
revengers.print_group()
