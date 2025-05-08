from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, damage, ammo_count):
        self.damage = damage
        self.ammo_count = ammo_count

    @abstractmethod
    def basic_attack(self):
        pass

    @abstractmethod
    def ultimate_attack(self):
        pass

    @abstractmethod
    def charge_weapon(self):
        pass


class Greatsword(Weapon):
    def __init__(self, damage, energy):
        super().__init__(damage, energy)
        self.energy_count = energy

    def basic_attack(self):
        if self.energy_count >= 5:
            self.energy_count -= 5
            print(f"You performed a Charged Slash! Damage: {self.damage} | Remaining energy: {self.energy_count}")
        else:
            print("Not enough energy for basic attack!")

    def ultimate_attack(self):
        if self.energy_count >= 15:
            self.energy_count -= 15
            print(f"⚔️ You performed True Charged Slash! Damage: {self.damage * 3} | Remaining energy: {self.energy_count}")
        else:
            print("Not enough energy for ultimate!")

    def charge_weapon(self):
        self.energy_count += 10
        print(f"You take a deep breath and rest. Gained +10 energy. Current energy: {self.energy_count}")

class Blasthammer(Weapon):
    def __init__(self, damage, blast_cores):
        super().__init__(damage, blast_cores)
        self.blast_cores = blast_cores

    def basic_attack(self):
        if self.blast_cores >= 1:
            self.blast_cores -= 1
            print(f"You leapt in the air for a Ground Pound! Damage: {self.damage} | Remaining blast cores: {self.blast_cores}")
        else:
            print("Not enough blast cores for basic attack!")

    def ultimate_attack(self):
        if self.blast_cores >= 3:
            self.blast_cores -= 3
            print(f"💥 Mighty Big Bang Erupts! Damage: {self.damage * 3} | Remaining blast cores: {self.blast_cores}")
        else:
            print("Not enough blast cores for ultimate!")

    def charge_weapon(self):
        self.blast_cores += 3
        print(f"You opened the canister and replaced its core. Gained +3 blast cores. Blast Cores: {self.blast_cores}")

class Rifle(Weapon):
    def __init__(self, damage, ammo_count, magazine_size):
        super().__init__(damage, ammo_count)
        self.magazine_size = magazine_size

    def basic_attack(self):
        if self.ammo_count >= 1:
            self.ammo_count -= 1
            print(f"You performed a three-round burst! Damage: {self.damage} | Remaining ammo: {self.ammo_count}")
        else:
            print("Not enough bullets left!")

    def ultimate_attack(self):
        if self.ammo_count >= 3:
            self.ammo_count -= 3
            print(f"🔫 Unloaded Bullet Storm! Total damage: {self.damage * 3} | Remaining ammo: {self.ammo_count}")
        else:
            print("Not enough bullets for ultimate!")

    def charge_weapon(self):
        self.ammo_count += self.magazine_size
        print(f"You slam a new magazine in and rack the slide. +{self.magazine_size} ammo loaded! Current ammo: {self.ammo_count}")


class Bow(Weapon):
    def __init__(self, damage, ammo_count, arrow_type):
        super().__init__(damage, ammo_count)
        self.arrow_type = arrow_type

    def basic_attack(self):
        if self.ammo_count >= 1:
            self.ammo_count -= 1
            print(f"You performed quickdraw using {self.arrow_type} arrow! Damage: {self.damage} | Remaining arrows: {self.ammo_count}")
        else:
            print("Not enough arrows left!")

    def ultimate_attack(self):
        if self.ammo_count >= 2:
            self.ammo_count -= 2
            print(f"🏹 Fired charged {self.arrow_type} piercer! Massive damage: {self.damage * 2} | Remaining arrows: {self.ammo_count}")
        else:
            print("Not enough arrows for ultimate!")

    def charge_weapon(self):
        self.ammo_count += 5
        print(f"You reach back and grab 5 more arrows from your quiver. Current arrows: {self.ammo_count}")


class MagicStaff(Weapon):
    def __init__(self, damage, mana, mana_cost, element_type):
        super().__init__(damage, mana)
        self.mana_cost = mana_cost
        self.element_type = element_type

    def basic_attack(self):
        if self.ammo_count >= 1:
            self.ammo_count -= 1
            print(f"You lobbed a {self.element_type} element projectile! Damage: {self.damage} | Remaining mana: {self.ammo_count}")
        else:
            print("Not enough mana for basic attack!")

    def ultimate_attack(self):
        if self.ammo_count >= self.mana_cost * 2:
            self.ammo_count -= self.mana_cost * 2
            print(f"☄️ Unleashed the {self.element_type} Tempest! Total damage: {self.damage * 4} | Remaining mana: {self.ammo_count}")
        else:
            print("Insufficient mana for ultimate attack!")

    def charge_weapon(self):
        self.ammo_count += 8
        print(f"You close your eyes and focus... +8 mana restored. Current mana: {self.ammo_count}")


class Gauntlets(Weapon):
    def __init__(self, damage, fury):
        super().__init__(damage, fury)
        self.fury = fury

    def basic_attack(self):
        if self.fury < 100:
            self.fury += 10
            if self.fury > 100:
                self.fury = 100  
            print(f"You punched the enemy! Damage: {self.damage} | Fury gained: 10 | Current fury: {self.fury}")
        else:
            print(f"You punched the enemy! Damage: {self.damage} | Fury is already at max: {self.fury}")

    def ultimate_attack(self):
        if self.fury >= 100:
            self.fury -= 100
            print(f"👊 You unleashed Cease and Desist! Massive damage: {self.damage * 3} | Fury consumed: 100 | Remaining fury: {self.fury}")
        else:
            print("Not enough fury to cast the ultimate!")

    def charge_weapon(self):
        self.fury += 30
        if self.fury > 100:
            self.fury = 100  
        print(f"You channel your anger. Fury restored: 30 | Current fury: {self.fury}")
    

# === Sample Usage ===

print("=== Rifle Test ===")
rifle = Rifle(50, 0, 10)
rifle.basic_attack() # Not enough ammo for basic attack and ultimate 
rifle.ultimate_attack()
rifle.charge_weapon() # Will perform attacks when theres enough after charging
rifle.basic_attack()
rifle.ultimate_attack()

print("\n=== Greatsword Test ===")
sword = Greatsword(150, 0)
sword.basic_attack()
sword.ultimate_attack()
sword.charge_weapon()
sword.basic_attack()
sword.charge_weapon()
sword.ultimate_attack()

print("\n=== Blasthammer Test ===")
hammer = Blasthammer(150, 0)
hammer.basic_attack()
hammer.ultimate_attack()
hammer.charge_weapon()
hammer.basic_attack()
hammer.charge_weapon()
hammer.ultimate_attack()

print("\n=== Bow Test ===")
bow = Bow(35, 0, "fire")
bow.basic_attack()
bow.ultimate_attack()
bow.charge_weapon()
bow.basic_attack()
bow.charge_weapon()
bow.ultimate_attack()

print("\n=== Magic Staff Test ===")
staff = MagicStaff(60, 0, 5, "ice")
staff.basic_attack()
staff.ultimate_attack()
staff.charge_weapon()
staff.basic_attack()
staff.charge_weapon()
staff.ultimate_attack()

print("\n=== Gauntlets Test ===")
gauntlets = Gauntlets(200, 0)
gauntlets.basic_attack()  
gauntlets.basic_attack()  
gauntlets.ultimate_attack()  
gauntlets.charge_weapon()  
gauntlets.ultimate_attack()  
gauntlets.basic_attack()  
gauntlets.basic_attack()  
gauntlets.charge_weapon()  
