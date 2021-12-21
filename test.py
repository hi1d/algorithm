class game:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.life = True

    def attack(self, 고블린):
        고블린.hp -= self.damage
        print(고블린.name, 고블린.hp, 고블린.damage)
        if 고블린.hp < 0:
            print("고블린이 죽었습니다.")
            고블린.life = False


고블린 = game('고블린', 50, 10)
print(고블린.name, 고블린.hp, 고블린.damage)
전사 = game('전사', 100, 30)
print(전사.name, 전사.hp, 전사.damage)
전사.attack(고블린)
