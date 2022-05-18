"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""

korko = 1.0117
tuki = float(input("Enter the amount of the study benefits: "))

raha1 = korko*tuki
raha2 = raha1*korko
print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be " + str(raha1) + " euros")
print("and if there was another index raise, the study")
print("benefits would be as much as "+ str(raha2) +" euros")