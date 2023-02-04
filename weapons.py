class Gun:
    def __init__(self,model, ammo) :
        self.model = model
        self.ammo = ammo
    def add_ammo(self,ammo):
        if self.ammo+ammo <=20:
            self.ammo+=ammo
    def fire_ammo(self):
        while self.ammo > 0:
            print('pew')
            if self.ammo>=0:
                self.ammo-=1