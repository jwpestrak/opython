"""
Namespace that catalogs the world's coconuts.
"""

class coconut(object):
    def __init__(self, species)
        self.coco_type = species
        if species == 'South Asian':
            self.weight = 3.0
        elif species == 'Middle Eastern':
            self.weight = 2.5
        elif species == 'American':
            self.weight = 3.5
        else:
            self.weight = 0.0 

class Inventory(object):
    
    coco_inv =  {}

    def add_coconut(self, coco_type):
        """
        Add a coconut to the inventory.
        """    
        if not isinstance(self, coconut):
            raise AttributeError
        if coco_type not in coco_inv.keys():
           coco_inv[coco_type] = 1
        else: 
           coco_inv[coco_type] += 1

    def total_weight(self):
        """
        Compute and return the total weight of the inventory.
        """
        weight = 0.0
        for k in coco_inv.keys():
            if k == 'south_asian':
                weight += 3.0     
            elif k == 'middle_eastern':
                weight += 2.5     
            elif k == 'american':
                weight += 3.5 
        return weight    

