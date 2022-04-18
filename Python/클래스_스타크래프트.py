#일반유닛
from random import randint


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        print("지상유닛이동")
        print("{0} : {1} 방향으로 이동. 속도 {2}".format(self.name, location, self.speed))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("파괴")

#공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name,hp, speed)
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다 공격력 {2}".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("파괴")

class MArine(AttackUnit):
    def __init__(self):
        super().__init__("마린", 50, 1, 5)
    #스팀팩 체력 10감소 스피드 공격력 5증가
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("스팀팩사용 10감소")
        else:
            print("체력부족 스팀팩 X")

class Tank(AttackUnit):
    siz_dev = False #시즈모드 개발여부    

    def __init__(self):
        super().__init__("탱크", 150, 1, 35)
        self.siz_mode = False
    
    def set_siz_mode(self):
        if tank.siz_dev == False:
            return
        
        if self.siz_mode == False:
            print("시즈모드 전환")
            self.damage *= 2
            self.siz_mode = True
        else:
            print("시즈모드 해제")
            self.damage /= 2
            self.siz_mode = False

class flyable:
    def __init__(self, fly_speed):
        self.fly_speed = fly_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. 속도 {2}".format(name, location, self.fly_speed))

class flyattack(AttackUnit, flyable) :
    def __init__(self, name, hp, damage, fly_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
        flyable.__init__(self, fly_speed)
    def move(self, location):
        print("공중유닛이동")
        self.fly(self.name, location)

class Wraith(flyattack):
    def __init__(self):
        super().__init__("레이스", 80, 20, 5)
        self.clocked = False

        def clock(self):
            if self.clocked == True:
                print("클록킹 해제")
                self.clocked == False
            else:
                print("클록킹 모드")
                self.clocked == True


def game_start():
    print("게임 시작")

def game_over():
    print("유다희")

# 게임을 해보자
game_start()    

m1 = MArine()
m2 = MArine()
m3 = MArine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.siz_dev = True
print("시즈모드 개발 완료")    

for unit in attack_units:
    if isinstance(unit, MArine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.siz_mode = True
    elif isinstance(unit, Wraith):
        unit.clocked = True

#전체 공격
for unit in attack_units:
    unit.attack("2시")

for unit in attack_units:
    unit.damaged(randint(5,21))

game_over()