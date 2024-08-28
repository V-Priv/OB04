from abc import ABC, abstractmethod
import random


# Абстрактный класс для оружия


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


# Конкретные типы оружия


class Sword(Weapon):
    def attack(self):
        damage = random.randint(5, 10)  # случайный выбор урона для здоровья монстра от 5 до 10
        print("Боец наносит удар мечом.")
        return damage

    def get_name(self):
        return "меч"


class Bow(Weapon):
    def attack(self):
        damage = random.randint(10, 20)  # случайный выбор урона для здоровья монстра от 10 до 20
        print("Боец наносит удар из лука.")
        return damage

    def get_name(self):
        return "лук"


class Axe(Weapon):
    def attack(self):
        damage = random.randint(20, 30)  # случайный выбор урона для здоровья монстра от 20 до 30
        print("Боец наносит удар топором.")
        return damage

    def get_name(self):
        return "топор"


class Gun(Weapon):
    def attack(self):
        damage = random.randint(30, 30)  # гарантированный урон монстру с одного выстрела
        print("Боец стреляет из пистолета.")
        return damage

    def get_name(self):
        return "пистолет"


# Класс бойца


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"Боец выбирает {self.weapon.get_name()}.")

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            print("Оружие не выбрано!")
            return 0


# Класс монстра


class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):  # метод нанесения урона здоровью монстра
        self.health -= damage
        print(f"{self.name} получает {damage} урона и у него остаётся {self.health} здоровья.")

    def is_alive(self):  # метод определения остатка здоровья монстра
        return self.health > 0


# Функция боя


def battle(fighter: Fighter, monster: Monster):
    print(f"Бой начинается между {fighter.name} и {monster.name}!")
    while monster.is_alive():
        damage = fighter.attack()
        monster.take_damage(damage)
        if not monster.is_alive():
            print(f"{monster.name} побеждён!")


# Функция для выбора оружия


def choose_weapon():
    weapons = {
        "1": Sword(),
        "2": Bow(),
        "3": Axe(),
        "4": Gun()
    }
    print("Выберите оружие:\n1. Меч\n2. Лук\n3. Топор\n4. Пистолет")
    choice = input("Введите номер оружия: ")
    return weapons.get(choice, None)


# Выполнение

if __name__ == "__main__":

    # Создание объектов классов Fighter и Monster

    fighter = Fighter("Герой")
    monster = Monster("Гоблин", 30)

    # Выбор оружия и проведение боя

    weapon = choose_weapon()
    if weapon:
        fighter.change_weapon(weapon)
        battle(fighter, monster)

    # Бой с другим оружием и монстром с другим именем
    if not monster.is_alive():
        monster = Monster("Орк", 30)
        weapon = choose_weapon()
        if weapon:
            fighter.change_weapon(weapon)
            battle(fighter, monster)
