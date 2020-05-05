class Item():

    def __init__(self, cesta_basica, higiene, gas_cozinha):
        self.cesta_basica = cesta_basica
        self.higiene = higiene
        self.gas_cozinha = gas_cozinha

item = Item('Cesta Basica', 'Kit Higiene', 'Botijão')
print(item.cesta_basica,item.gas_cozinha,item.higiene)