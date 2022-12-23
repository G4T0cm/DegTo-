import os
import subprocess 
import sys

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
#Esto para hacer hueco que queda muy feo en verdas
#Un saludito a Lykos
prGreen("""\
 _____               _           ___  
 |  __ \             | |         / _ \ 
 | |  | | ___  __ _  | |_ ___   | (_) |
 | |  | |/ _ \/ _` | | __/ _ \   \___/ 
 | |__| |  __/ (_| | | || (_) | 
 |_____/ \___|\__, |  \__\___/         
               __/ |                   
              |___/ 
                    """)

prCyan("Iphone GPS Location to Google maps converter ")
prYellow("Created by G4T0 & Frodox ")

x = input('Insert Cords:')

cords = (x)

resultado = cords.replace('DEG', 'º')
result = ''
s = (resultado.replace(' ', ''))
print("Google Maps coords: ", s)

subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:]) #restart the program