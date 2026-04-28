import random
import time

jobList = ["戦士","魔法使い","アーチャー"]
hpList = [200,100,150]
maxHpList = [200,100,150]
attackList = [70,100,60]
gardList = [30,10,20]
avoidanceList = [10,20,35]
sutaminaList = [5,2,3]

class character:
    def __init__(self,name,job,hp,maxHp,attack,gard,avoidance,sutamina):
        self.name = name
        self.job = job
        self.hp = hp
        self.maxHp = maxHp
        self.attack = attack
        self.gard = gard
        self.avoidance = avoidance
        self.sutamina = sutamina

    def showStatus(self):
        print(f"----ステータス----")
        print(f"名前:{self.name}")
        print(f"職業:{self.job}")
        print(f"HP:{self.hp} / {self.maxHp}")
        print(f"攻撃力:{self.attack}  防御力:{self.gard}  回避率:{self.avoidance}%  スタミナ:{self.sutamina}")
    
    def battleAction(self,choice):
        reSutamina = self.sutamina
        if choice == 1:
            self.sutamina -= 2
            if self.sutamina < 0:
                self.sutamina = reSutamina + 1
                print(f"{self.name}は攻撃を選んだ")
                time.sleep(1.5)
                print(f"しかしスタミナが足りない！(スタミナ +1)")
                return 0
            else:
                print(f"{self.name}は攻撃を選んだ(スタミナ -2)")
                return 1
        elif choice == 2:
            self.sutamina += 3
            print(f"{self.name}は防御を選んだ(スタミナ +3)")
            return 2
        else:
            self.sutamina += 1
            if self.sutamina < 0:
                self.sutamina = reSutamina + 1
                print(f"{self.name}は攻撃を選んだ")
                time.sleep(1.5)
                print(f"しかしスタミナが足りない！(スタミナ +1)")
                return 0
            else:
                print(f"{self.name}は回避を選んだ(スタミナ +1)")
                return 3

def battleShowStatus(Hero,enemy):
    print("------------")
    print(f"{Hero.name} HP:{Hero.hp} / {Hero.maxHp}  スタミナ:{Hero.sutamina}")
    print(f"{enemy.name} HP;{enemy.hp} / {enemy.maxHp}  スタミナ:{enemy.sutamina}")
    print("------------")

        
print(f"名前を入力してください")
nameInput = input()
time.sleep(1.5)
print("")
print(f"職業を選んでください")
for i in range(len(jobList)):
    time.sleep(1.5)
    print("")
    print(f"{i+1}{jobList[i]}(HP:{hpList[i]} 攻撃力:{attackList[i]} 防御力:{gardList[i]} 回避率:{avoidanceList[i]}%)")
print("")
time.sleep(1.5)
jobInput = int(input("番号:"))-1

Hero = character(nameInput,jobList[jobInput],hpList[jobInput],maxHpList[jobInput],attackList[jobInput],gardList[jobInput],avoidanceList[jobInput],sutaminaList[jobInput])

Hero.showStatus()
print("")
time.sleep(1.5)

enemy = character("スライム","モンスター",120,120,40,10,5,5)
print(f"{enemy.name}が現れた!")
print(f"")
time.sleep(1.5)
enemy.showStatus()
time.sleep(1.5)
print(f"")
print(f"----バトル開始----")
print("")
time.sleep(1.5)

while True:
    battleShowStatus(Hero,enemy) 
    print("")
    print(f"{Hero.name}のターン")
    time.sleep(1.5)
    print(f"1:攻撃({Hero.attack} スタミナ-2)  2:防御({Hero.gard} スタミナ+3)  3:回避({Hero.avoidance}% スタミナ+1)")
    time.sleep(1.5)
    choice = int(input("どれを選ぶ？ 番号:"))
    time.sleep(1.5)
    HeroChoice = Hero.battleAction(choice)
    time.sleep(1.5)

    if HeroChoice == 0:
        p
    elif HeroChoice == 1:
        print(f"{enemy.name}のターン")
        choice = random.randint(1,3)
        time.sleep(1.5)
        enemyChoice = enemy.battleAction(choice)
        damage = max(0,Hero.attack - enemy.gard)
        if enemyChoice == 0:
            print(f"{enemy.name}はスタミナが足りず行動できない")
            time.sleep(1.5)
            print(f"{Hero.name}の攻撃！")
            time.sleep(1.5)
            enemy.hp -= damage
            print(f"{enemy.name}は{damage}ダメージを受けた")
            time.sleep(1.5)
            if Hero.hp <= 0 or enemy.hp <= 0:
                break
        elif enemyChoice == 1:
            print(f"{Hero.name}の攻撃！")
            time.sleep(1.5)
            enemy.hp -= damage
            print(f"{enemy.name}は{damage}ダメージを受けた")
            time.sleep(1.5)
            if Hero.hp <= 0 or enemy.hp <= 0:
                break
            print(f"{enemy.name}の攻撃！")
            time.sleep(1.5)
            Hero.hp -= enemy.attack
            print(f"{Hero.name}は{enemy.attack}ダメージを受けた")
            time.sleep(1.5)
            if Hero.hp <= 0 or enemy.hp <= 0:
                break

        elif enemyChoice == 2:
            print(f"{Hero.name}の攻撃！")
            time.sleep(1.5)
            print(f"{enemy.name}は守った")
            time.sleep(1.5)
            if damage > 0:
                enemy.hp -= damage
                print(f"{enemy.name}は{damage}ダメージを受けた")
                time.sleep(1.5)
            if Hero.hp <= 0 or enemy.hp <= 0:
                break
            else:
                print(f"{enemy.name}は攻撃を受け止めた")
                time.sleep(1.5)
            
        elif enemyChoice == 3:
            print(f"{Hero.name}の攻撃！")
            time.sleep(1.5)
            avoid = random.randint(1,100)
            if avoid < enemy.avoidance:
                print(f"{enemy.name}は避けた")
                time.sleep(1.5)
            else:
                print(f"{enemy.name}は避けれなかった。")
                time.sleep(1.5)
                print(f"{enemy.name}は{damage}ダメージを受けた")
                time.sleep(1.5)
            if Hero.hp <= 0 or enemy.hp <= 0:
                break

    elif HeroChoice == 2:
        choice = 1
        enemyChoice = enemy.battleAction(choice)
        damage = max(0,enemy.attack - Hero.gard)

        if enemyChoice == 0:
            print(f"{enemy.name}はスタミナが足りず攻撃に失敗した")
            time.sleep(1.5)
        else:
            print(f"{enemy.name}の攻撃")
            time.sleep(1.5)
            print(f"{Hero.name}は{damage}ダメージを受けた")
            time.sleep(1.5)
            if Hero.hp <= 0 or enemy.hp <= 0:
                break

    else:
        choice = 1
        enemyChoice = enemy.battleAction(choice)
        damage = max(0,enemy.attack - Hero.gard)

        if enemyChoice == 0:
            print(f"{enemy.name}はスタミナが足りず攻撃に失敗した")
            time.sleep(1.5)
        else:
            print(f"{enemy.name}の攻撃")
            time.sleep(1.5)
            if random.randint(1,100) < Hero.avoidance:
                print(f"{Hero.name}は避けた")
                time.sleep(1.5)
            else:
                print(f"{Hero.name}は避けれなかった。")
                time.sleep(1)
                print(f"{Hero.name}は{damage}ダメージを受けた")
                time.sleep(1.5)
            if Hero.hp <= 0 or enemy.hp <= 0:
                break   

if Hero.hp > 0:
    print(f"{Hero.name}の勝利!")
else:
    print(f"{Hero.name}は死んだ")