class Equipment:

    def __init__(self, name):
        self.name = name

class Inventory:

    def __init__(self):
        self.inventory = []

    def add_equipment(self, equipment):
        if len(self.inventory) <= 50:
            self.inventory.append(equipment)
            return f"{equipment.name} добавлено в инвентарь"
        else:
            return "У вас недостаточно место в инвентаре"
        
    def remove_equipment(self, equipment):
        if equipment in self.inventory:
            self.inventory.remove(equipment)
            return f"{equipment.name} удалено из вашего инвентаря"
        else:
            return "У вас в инвентаре не такого веща"
        
x = Equipment("sword")
y = Inventory()

print(y.add_equipment(x))
print(y.remove_equipment(x))
