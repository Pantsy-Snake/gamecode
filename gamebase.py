Skip to content
Pantsy-Snake/gamebase.py
Created 30 minutes ago
Code
Revisions
1
unfinished text-game
gamebase.py
import random
from time import sleep

level = 0
response = True
maxdmg = 10
mindmg = 1
maxhp = 50
hp = maxhp
heal = round(maxhp*0.4)
ripperhp = 15 + level+1
ripperdmg = 30 + level*2
brutehp = 35 + level*3
brutedmg = 15 + round(level*1.5)
sparkerhp = 25 + level
sparkerdmg = 20 + level
assassinhp = 10 + level+1
assassindmg = 20 + level+1
assassincritch = 0
battle = False
enemy = 0
point = 0
hlnd = 0
already = False
answer = ""

def main(level,maxhp,hp):
    print("afterwards", maxhp)
    level
    response = True
    maxdmg
    mindmg
    maxhp
    hp
    heal = round(maxhp*0.4)
    ripperhp = 15 + level
    ripperdmg = 30 + level*2
    brutehp = 35 + level*3
    brutedmg = 15 + level
    sparkerhp = 25 + level
    sparkerdmg = 20 + level
    assassinhp = 10 + level+1
    assassindmg = 20 + level+1
    assassincritch = 0
    battle = False
    enemy = 0
    point = 0
    hlnd = 0
    already = False
    answer = ""

    print("Aftertheafter", maxhp)
    answer = input("Read the Dungeon Guide? y/n: ") 
    if answer == "y":
        print("This is the Dungeon Guide."); sleep(1)
        print("You: You are level:", level, "\nYou currently have", hp,"/",maxhp, "Health and deal", mindmg, "-", maxdmg, "damage.\nAs you kill enemies, you will descend further into the dungeon, where you grow stronger but your enemies do too."); sleep(2)
        print("During battle, you can type 'a' to attack or 'h' to heal. Healing also reduces the damage you take from the next attack by half."); sleep(2)
        print("Enemies: \n The RIPPER: \n The RIPPER is a dark being that tears away at your very soul, dealing high amounts of damage, \n but is very fragile."); sleep(2)
        print("The BRUTE: \n The BRUTE is a massive humanoid being that has endured years of toruture, so it can take quite a bit of damage, \n however they don't deal much dmaage themselves."); sleep(2)
        print("The SPARKER: \n The SPARKER is a ball of electrical energy, manifested from the souls of adventurers that have died in this dungeon. \n The SPARKER does not gain strength as you level up as much as other enemies."); sleep(2)
        print("The ASSASSIN: \n The ASSASSIN is an adventurer who has taken to killing and robbing other adventurers that travel down into the dungeon. \n The ASSASSIN has a chance to deal a critical hit and dodge attacks."); sleep(2)
    elif answer == "n":
        print("You are now approaching an enemy..."); sleep(2)
        already = True
        battle = True
    if already == False:
     already = True
     print("You are now approaching an enemy..."); sleep(2)
     battle = True
    enemy = random.randint(1,4)
    if enemy == 1:
        print("A Ripper Is In Your Path."); sleep(1)
    while enemy == 1:
        if ripperhp<=0:
            enemy = 0
            battle = False
            already = False
            print("You defeated the Ripper, you leveled up.")
            point = 1
        elif enemy == 1:
            ah = input("Attack or Heal? a/h: ")
            if ah == "a":
                hlnd = 0
                cdmg = random.randint(mindmg,maxdmg)
                ripperhp-=cdmg
                print("You dealt", cdmg, "damage."); sleep(2)
                if ripperhp<=0:
                    enemy = 0
                    battle = False
                    already = False
                    print("You defeated the Ripper, you leveled up.")
                    point = 1
                elif battle == True:
                        crdmg = random.randint(level+5,ripperdmg)
                        hp-=crdmg
                        print("The Ripper struck you for", crdmg, "damage."); sleep(1)                        
                        if hp<=0:
                            print("You Died")
                            exit() 
                        print("You have", hp, "Health.")
            elif ah == "h":
                    if hlnd == 0:
                            hlnd = 1
                            hp+=heal
                            if hp>maxhp:
                                hp = maxhp
                            print("You healed for", heal, "Health and are going to reduce the damage of the enemy's next attack"); sleep(2)
                            print("You have", hp, "Health")
                            crdmg = random.randint(level+5,ripperdmg)
                            crdmg = round(crdmg*0.5)
                            hp-=crdmg
                            print("The Ripper struck you for", crdmg, "damage."); sleep(1)
                    if hp<=0:
                        print("You Died")
                        exit()
                    print("You have", hp, "Health.")
            elif hlnd !=0:
                    print("You Cannot Heal Two Turns In A Row. You Must Attack This Turn.")
    if enemy == 2:
         print("A Brute Is In Your Path."); sleep(1)
    while enemy == 2:
            if brutehp<=0:
                 enemy = 0
                 battle = False
                 already = False
                 print("You defeated the Brute, you leveled up.")
                 point = 1
            elif enemy == 2:
                ah = input("Attack or Heal? a/h: ")
                if ah == "a":
                    hlnd = 0
                    cdmg = random.randint(mindmg,maxdmg)
                    brutehp-=cdmg
                    print("You dealt", cdmg, "damage."); sleep(2)
                    if brutehp<=0:
                     enemy = 0
                     battle = False
                     already = False
                     print("You defeated the Brute, you leveled up.")
                     point = 1
                    elif battle == True:
                         crdmg = random.randint(level+2,brutedmg)
                         hp-=crdmg
                         print("The Brute punched you for", crdmg, "damage."); sleep(1)
                         if hp<=0:
                            print("You Died")
                            exit() 
                         print("You have", hp, "Health.")
                elif ah == "h":
                    if hlnd == 0:
                            hlnd = 1
                            hp+=heal
                            if hp>maxhp:
                                hp = maxhp
                            print("You healed for", heal, "Health and are going to reduce the damage of the enemy's next attack"); sleep(2)
                            print("You have", hp, "Health")
                            crdmg = random.randint(level+2,brutedmg)
                            crdmg = round(crdmg*0.5)
                            hp-=crdmg
                            print("The Brute punched you for", crdmg, "damage."); sleep(1)
                    if hp<=0:
                        print("You Died")
                        exit()
                    print("You have", hp, "Health.")
                elif hlnd !=0:
                    print("You Cannot Heal Two Turns In A Row. You Must Attack This Turn.")
    if enemy == 3:
         print("A Sparker Is In Your Path."); sleep(1)
    while enemy == 3:
            if sparkerhp<=0:
                     enemy = 0
                     battle = False
                     already = False
                     print("You defeated the Sparker, you leveled up.")
                     point = 1
            elif enemy == 3:
                ah = input("Attack or Heal? a/h: ")
                if ah == "a":
                    hlnd = 0
                    cdmg = random.randint(mindmg,maxdmg)
                    sparkerhp-=cdmg
                    print("You dealt", cdmg, "damage."); sleep(2)
                    if sparkerhp<=0:
                     enemy = 0
                     battle = False
                     already = False
                     print("You defeated the Sparker, you leveled up.")
                     point = 1
                    elif battle == True:
                         crdmg = random.randint(level+4,sparkerdmg)
                         hp-=crdmg
                         print("The Sparker projected energy at you for", crdmg, "damage."); sleep(1)
                         if hp<=0:
                            print("You Died")
                            exit()
                         print("You have", hp, "Health.")
                elif ah == "h":
                    if hlnd == 0:
                            hlnd = 1
                            hp+=heal
                            if hp>maxhp:
                                hp = maxhp
                            print("You healed for", heal, "Health and are going to reduce the damage of the enemy's next attack"); sleep(2)
                            print("You have", hp, "Health")
                            crdmg = random.randint(level+4,sparkerdmg)
                            crdmg = round(crdmg*0.5)                
                            hp-=crdmg
                            print("The Sparker projected energy at you for", crdmg, "damage."); sleep(1)
                    if hp<=0:
                        print("You Died")
                        exit()
                    print("You have", hp, "Health.")
                elif hlnd !=0:
                    print("You Cannot Heal Two Turns In A Row. You Must Attack This Turn.")
    if enemy == 4:
         print("An Assassin Is In Your Path."); sleep(1)
    while enemy == 4:
            if assassinhp<=0:
                     enemy = 0
                     battle = False
                     already = False
                     print("You defeated the Assassin, you leveled up.")
                     point = 1
            elif enemy == 4:
                ah = input("Attack or Heal? a/h: ")
                if ah == "a":
                    dodge = random.randint(0,1)
                    hlnd = 0
                    if dodge == 0:
                        cdmg = random.randint(mindmg,maxdmg)
                        assassinhp-=cdmg
                        print("You dealt", cdmg, "damage."); sleep(2)
                    elif dodge == 1:
                         print("The Assassin Dodged Your Attack."); sleep(2)
                    if assassinhp<=0:
                     enemy = 0
                     battle = False
                     already = False
                     print("You defeated the Assassin, you leveled up.")
                     point = 1
                    elif battle == True:
                         crdmg = random.randint(level+5,assassindmg)
                         assassincritch = random.randint(0,2)
                         if assassincritch == 1:
                              crdmg = crdmg*2
                              hp-=crdmg
                              print("The Assassin Crit You For", crdmg, "damage.")
                         elif assassincritch != 1:
                              hp-=crdmg
                              print("The Assassin cut you for", crdmg, "damage."); sleep(1)
                         if hp<=0:
                            print("You Died")
                            exit()
                         print("You have", hp, "Health.") 
                elif ah == "h":
                    if hlnd == 0:
                            hlnd = 1
                            hp+=heal
                            if hp>maxhp:
                                hp = maxhp
                            print("You healed for", heal, "Health and are going to reduce the damage of the enemy's next attack"); sleep(2)
                            print("You have", hp, "Health")
                            crdmg = random.randint(level+5,assassindmg)
                            crdmg = round(crdmg*0.5)
                            assassincritch = random.randint(0,2)
                            if assassincritch == 1:
                                  crdmg = crdmg*2
                                  hp-=crdmg
                                  print("The Assassin Crit You For", crdmg, "damage.")
                            elif assassincritch != 1:
                                hp-=crdmg
                                print("The Assassin cut you for", crdmg, "damage."); sleep(1)
                    if hp<=0:
                        print("You Died")
                        exit()
                    print("You have", hp, "Health.")
                elif hlnd !=0:
                    print("You Cannot Heal Two Turns In A Row. You Must Attack This Turn.")
    while point == 1:
            if point == 1:
                print("You have a point to spend in either; Your Health, Minimum Damage, Maximum Damage, Crit Chance, Dodge Chance, or you can gain a magic spell"); sleep(2)
                spend = input("Type the number corresponding to what you want to upgrade\n1: Upgrade your Health by 5.\n2: Upgrade your Minimum Damage by 2.\n3: Upgrade ypur Maximum Damage by 3.\n4: Upgrade your Crit Chance by 5%.\n5: Upgrade your Dodge Chance by 4%.\n6: Gain a Spell.\n>")
            if spend == "1":
                point = 0
                maxhp = maxhp+5
                hp = hp+5
                print(maxhp)
                print("You descend further into the dungeon..."); sleep(2)
while response:            
 main(level+1,maxhp+5,hp+5)
Comment
 
Leave a comment
 
Footer
© 2024 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact
Manage cookies
Do not share my personal information
unfinished text-game
