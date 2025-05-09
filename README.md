# ⚔️ LAB ACTIVITY 3 - GROUP 10: Weapons

### Made by:

* **Caraig, Hans Gadiel P.**
* **Larga, Erika Ysobelle U.**
* **Mendoza, Goldwyn Daine Kierzene D.**
* **Ricohermoso, Lordy Miles J.**

---

## 🔍 Short Description

**⚔️ Weapon System Simulation ⚔️**
This project showcases a simple object-oriented weapon system in Python using abstract base classes, inheritance, and polymorphism. It demonstrates how different types of weapons share common interfaces while providing unique behaviors.

---

## ✨ Features

* **Abstract Base Class (`Weapon`)**
  Defines a common interface for all weapons.

* **⚔️ Six Concrete Weapon Classes ⚔️**

  * 🗡️ **Greatsword** – Uses energy for powerful melee attacks.
  * ⚒️ **Blasthammer** – Consumes blast cores to deal explosive damage.
  * 🔫 **Rifle** – Uses bullets and has a magazine reload system.
  * 🏹 **Bow** – Uses arrows of different types.
  * 🥊 **Magic Staff** – Casts spells using mana and supports elemental magic.
  * 👊 **Gauntlets** – Builds up Fury through melee attacks for a powerful finisher.

---

## 🧠 Object-Oriented Concepts Used

* **Abstraction**
  Common weapon behavior is defined in the abstract `Weapon` class.

* **Encapsulation**
  Weapon attributes like `ammo_count`, `damage`, etc. are managed within each class.

* **Inheritance**
  All weapon types inherit from the `Weapon` abstract base class.

* **Polymorphism**
  All weapon types implement the same methods (`basic_attack`, `ultimate_attack`, `charge_weapon`) with different behaviors.

---

## 🔁 Sample Usage

Each weapon is tested in scenarios such as:

* 🪫 **Insufficient resources**
* 🚀 **Charging / Reloading the weapon**
* 💥 **Performing attacks when resources are sufficient**

---

## 🛠️ How to Start the Program

### ▶️ Steps to Run

1. Open your terminal or command prompt.
2. Navigate to the folder where `weaponclass.py` is located.
3. Run the script:

   ```bash
   python weaponclass.py
   ```
4. Follow the on-screen prompts:

   * Choose a weapon by entering a number (1 to 6).
   * Customize values like damage, ammo, mana, etc., depending on your selected arsenal.
   * The program will then simulate the weapon in action.

---

## 🔁 Sample Interaction

```text
Select a weapon to test:
1 - Greatsword
2 - Blasthammer
3 - Rifle
4 - Bow
5 - Magic Staff
6 - Gauntlets

Enter the number of your choice: 3
Enter damage per shot for Rifle: 50
Enter starting ammo: 5
Enter magazine size: 10

--- Weapon Test ---
You performed a three-round burst! Damage: 50 | Remaining ammo: 4
Not enough bullets for ultimate!
You slam a new magazine in and rack the slide. +10 ammo loaded! Current ammo: 14
You performed a three-round burst! Damage: 50 | Remaining ammo: 13
Unloaded Bullet Storm! Total damage: 150 | Remaining ammo: 10
```

---

## 🙏 Acknowledgement

We would like to express our deepest gratitude to our **CS 121 instructor, Ms. Fatima Marie Agdon**, for giving light to the essential concepts we used to build this project.

To all the people involved who helped bring this project to fruition — thank you.

Lastly, we would like to acknowledge ourselves for making it this far and for continuing to strive in our pursuit of success.
