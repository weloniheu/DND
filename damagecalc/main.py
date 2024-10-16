import random
import tkinter

numToTest = 10000
numTested = 0
subTotals = 0
damageDone = []
# Don't touch these


top = tkinter.Tk()

GWM = tkinter.IntVar()
WE = tkinter.IntVar()
advantageToggle = tkinter.IntVar()
disadvantageToggle = tkinter.IntVar()
reroll1and2 = tkinter.IntVar()

playerProf = tkinter.IntVar()

playerToHit = tkinter.IntVar()
targetAC = tkinter.IntVar()

critRange = tkinter.IntVar()

flatModifier = tkinter.IntVar()

diceToTest4 = tkinter.IntVar()
diceToTest6 = tkinter.IntVar()
diceToTest8 = tkinter.IntVar()
diceToTest10 = tkinter.IntVar()
diceToTest12 = tkinter.IntVar()

diceToTest4Crit = tkinter.IntVar()
diceToTest6Crit = tkinter.IntVar()
diceToTest8Crit = tkinter.IntVar()
diceToTest10Crit = tkinter.IntVar()
diceToTest12Crit = tkinter.IntVar()

tkinter.Checkbutton(top, text = "Do you have advantage?",
                    variable = advantageToggle).pack()
tkinter.Checkbutton(top, text = "Do you have disadvantage?",
                    variable = disadvantageToggle).pack()
tkinter.Checkbutton(top, text = "Do you have Weapon Expert active?",
                    variable = WE).pack()
tkinter.Checkbutton(top, text = "Can you reroll 1s and 2s?",
                    variable = reroll1and2).pack()
tkinter.Checkbutton(top, text = "Do you have Great Weapon Master active?",
                    variable = GWM).pack()

f5 = tkinter.Frame(top)
tkinter. Label(f5, text = "What is your proficiency bonus?").grid(row = 2, column = 0)
tkinter.Entry(f5, textvariable = playerProf).grid(row = 2, column = 1)
f5.pack()


f3 = tkinter.Frame(top)
tkinter.Label(f3, text = 'Minimum roll to crit').grid(row = 1, column = 0)
critBox = tkinter.Entry(f3, textvariable = critRange).grid(row = 1, column = 1)
critRange.set(20)
f3.pack()

#tkinter.Label(top, text = '').pack()
tkinter.Label(top, text = 'Regular attacks: Calculate the total number of each dice').pack()
f1 = tkinter.Frame(top)
tkinter.Label(f1, text = 'How many d4: ').grid(row = 1, column = 0)
tkinter.Entry(f1, textvariable = diceToTest4).grid(row = 1, column = 1)
tkinter.Label(f1, text = 'How many d6: ').grid(row = 2, column = 0)
tkinter.Entry(f1, textvariable = diceToTest6).grid(row = 2, column = 1)
tkinter.Label(f1, text = 'How many d8: ').grid(row = 3, column = 0)
tkinter.Entry(f1, textvariable = diceToTest8).grid(row = 3, column = 1)
tkinter.Label(f1, text = 'How many d10: ').grid(row = 4, column = 0)
tkinter.Entry(f1, textvariable = diceToTest10).grid(row = 4, column = 1)
tkinter.Label(f1, text = 'How many d12: ').grid(row = 5, column = 0)
tkinter.Entry(f1, textvariable = diceToTest12).grid(row = 5, column = 1)
f1.pack()

# tkinter.Label(top, text = '').pack()
tkinter.Label(top, text = 'Critical attacks: Calculate the total number of each dice for a crit').pack()
f2 = tkinter.Frame(top)
tkinter.Label(f2, text = 'How many d4: ').grid(row = 1, column = 0)
tkinter.Entry(f2, textvariable = diceToTest4Crit).grid(row = 1, column = 1)
tkinter.Label(f2, text = 'How many d6: ').grid(row = 2, column = 0)
tkinter.Entry(f2, textvariable = diceToTest6Crit).grid(row = 2, column = 1)
tkinter.Label(f2, text = 'How many d8: ').grid(row = 3, column = 0)
tkinter.Entry(f2, textvariable = diceToTest8Crit).grid(row = 3, column = 1)
tkinter.Label(f2, text = 'How many d10: ').grid(row = 4, column = 0)
tkinter.Entry(f2, textvariable = diceToTest10Crit).grid(row = 4, column = 1)
tkinter.Label(f2, text = 'How many d12: ').grid(row = 5, column = 0)
tkinter.Entry(f2, textvariable = diceToTest12Crit).grid(row = 5, column = 1)

f2.pack()

f4 = tkinter.Frame(top)
# tkinter.Label(f4, text = '').grid(row = 0, column = 0)
tkinter.Label(f4, text = 'What is your flat damage modifier?').grid(row = 1, column = 0)
tkinter.Entry(f4, textvariable = flatModifier).grid(row = 1, column = 1)
f4.pack()

tkinter.Label(top, text = 'Note: If you are using Great Weapon Master do not include the damage bonus in this field').pack()

# tkinter.Label(top, text = '').pack()
tkinter.Label(top, text = 'You only need to fill these in if you want to include chance to hit').pack()

f6 = tkinter.Frame(top)
tkinter.Label(f6, text = 'What is your bonus to hit?').grid(row = 2, column = 0)
tkinter.Entry(f6, textvariable = playerToHit).grid(row = 2, column = 1)
tkinter.Label(f6, text = 'What is the target AC?').grid(row = 3, column = 0)
tkinter.Entry(f6, textvariable = targetAC).grid(row = 3, column = 1)
f6.pack()

tkinter.Button(top, text = "Click here to finish", command = top.destroy).pack()
top.mainloop()

def Main(numToTest, damageDone, diceToTest4, diceToTest6, diceToTest8, diceToTest10, diceToTest12,
     flatModifier, reroll1and2, advantageToggle, disadvantageToggle, playerToHit, targetAC,
     diceToTest4Crit, diceToTest6Crit, diceToTest8Crit, diceToTest10Crit, diceToTest12Crit, critRange):
    numTested = 0
    while numTested < numToTest:
        if advantageToggle:
            diceRolled = advantageRoller()
        elif disadvantageToggle:
            diceRolled = disadvantageRoller()
        else:
            diceRolled = random.randint(1,20)
        
        if diceRolled >= critRange:
            damageDone.append(Damage(diceToTest4Crit, diceToTest6Crit, diceToTest8Crit, diceToTest10Crit,
                                     diceToTest12Crit, flatModifier, reroll1and2))
        elif (diceRolled + playerToHit) >= targetAC:
            damageDone.append(Damage(diceToTest4, diceToTest6, diceToTest8, diceToTest10, diceToTest12,
                                     flatModifier, reroll1and2))
        else:
            damageDone.append(0)
        numTested += 1
    Printer(damageDone)

def advantageRoller():
    x = random.randint(1,20)
    y = random.randint(1,20)
    if x > y:
        return x
    else:
        return y
    
def disadvantageRoller():
    x = random.randint(1,20)
    y = random.randint(1,20)
    if x < y:
        return x
    else:
        return y
    
def Damage(diceToTest4, diceToTest6, diceToTest8, diceToTest10, diceToTest12, flatModifier, reroll1and2):
    diceRolled = 0
    subTotals = 0
    rolledNum = 0
    while diceRolled < diceToTest4:
        diceRolled += 1
        rolledNum = random.randint(1, 4)
        if rolledNum == 1 or rolledNum == 2:
            if reroll1and2 == True:
                rolledNum = random.randint(1, 4)
                
        if WE == True:
            rolledNum2 = random.randint(1,4)
            if rolledNum2 > rolledNum:
                rolledNum = rolledNum2
        subTotals += rolledNum
                
    diceRolled = 0
    while diceRolled < diceToTest6:
        diceRolled += 1
        rolledNum = random.randint(1, 6)
        if rolledNum == 1 or rolledNum == 2:
            if reroll1and2 == True:
                rolledNum = random.randint(1, 6)
        if WE == True:
            rolledNum2 = random.randint(1,6)
            if rolledNum2 > rolledNum:
                rolledNum = rolledNum2
        subTotals += rolledNum
        
    diceRolled = 0
    while diceRolled < diceToTest8:
        diceRolled += 1
        rolledNum = random.randint(1, 8)
        if rolledNum == 1 or rolledNum == 2:
            if reroll1and2 == True:
                rolledNum = random.randint(1, 8)
        if WE == True:
            rolledNum2 = random.randint(1,8)
            if rolledNum2 > rolledNum:
                rolledNum = rolledNum2
        subTotals += rolledNum
        
    diceRolled = 0
    while diceRolled < diceToTest10:
        diceRolled += 1
        rolledNum = random.randint(1, 10)
        if rolledNum == 1 or rolledNum == 2:
            if reroll1and2 == True:
                rolledNum = random.randint(1, 10)
        if WE == True:
            rolledNum2 = random.randint(1,10)
            if rolledNum2 > rolledNum:
                rolledNum = rolledNum2
        subTotals += rolledNum
        
    diceRolled = 0
    while diceRolled < diceToTest12:
        diceRolled += 1
        rolledNum = random.randint(1, 12)
        if rolledNum == 1 or rolledNum == 2:
            if reroll1and2 == True:
                rolledNum = random.randint(1, 12)
        if WE == True:
            rolledNum2 = random.randint(1,12)
            if rolledNum2 > rolledNum:
                rolledNum = rolledNum2
        subTotals += rolledNum
    return(subTotals + flatModifier)
    
def Printer(damageDone):
    print(sum(damageDone) / numToTest)

    
GWM = GWM.get()
WE = WE.get()
advantageToggle = advantageToggle.get()
disadvantageToggle = disadvantageToggle.get()
reroll1and2 = reroll1and2.get()

playerProf = playerProf.get()

playerToHit = playerToHit.get()
targetAC = targetAC.get()

critRange = critRange.get()

diceToTest4 = diceToTest4.get()
diceToTest6 = diceToTest6.get()
diceToTest8 = diceToTest8.get()
diceToTest10 = diceToTest10.get()
diceToTest12 = diceToTest12.get()

diceToTest4Crit = diceToTest4Crit.get()
diceToTest6Crit = diceToTest6Crit.get()
diceToTest8Crit = diceToTest8Crit.get()
diceToTest10Crit = diceToTest10Crit.get()
diceToTest12Crit = diceToTest12Crit.get()

if GWM == True:
    playerToHit -= playerProf
    flatModifier = playerProf*2 + flatModifier.get()
else:
    flatModifier = flatModifier.get()

Main(numToTest, damageDone, diceToTest4, diceToTest6, diceToTest8, diceToTest10, diceToTest12,
     flatModifier, reroll1and2, advantageToggle, disadvantageToggle, playerToHit, targetAC,
     diceToTest4Crit, diceToTest6Crit, diceToTest8Crit, diceToTest10Crit, diceToTest12Crit, critRange)


