import os
import subprocess 
import sys
# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
#Esto para hacer hueco que queda muy feo en verdas
#Un saludito a Lykos
print (gren+b+"""
  _____               _           ___  
 |  __ \             | |         / _ \ 
 | |  | | ___  __ _  | |_ ___   | (_) |
 | |  | |/ _ \/ _` | | __/ _ \   \___/ 
 | |__| |  __/ (_| | | || (_) | 
 |_____/ \___|\__, |  \__\___/         
               __/ |                   
              |___/ 
"""+b+gren)

print (cyan+b+"              [[ Iphone GPS Location to Google maps converter ]]"+b+gren)
print (" ")
print (red+b+"        (Created By G4T0 & Frodox)"+b+yellow)
print (" ")

x = input('Insert Coords:')

cords = (x)

resultado = cords.replace('DEG', 'º')
result = ''
s = (resultado.replace(' ', ''))
print("Google Maps coords: ", s)

subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:]) #restart the program
