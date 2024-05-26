import pyxel
import random

pyxel.init(250, 100, title="Jeu du dino", fps=30)
# Taille représentant le dino
dinoTaille = 24
# Position en Y du dino (en bas de la fenêtre)
dinoY = pyxel.height - dinoTaille
# Vitesse en Y du dino (au départ nulle)
dinoX = 16
dinoVit = 0
# Force de gravité qui ramène le dino vers le bas
dinoGravite = 1.7
# Position en Y du sol (au départ là où se trouve le dino)
solY = dinoY
# initialisation des ennemis
cactus_liste = []
# statut du jeu (0:joue, 1:start, 2:perdu, 3:gagné)
playing = 1
# nombre de frames depuis le début de la partie
frames = 0
# Animation
imagePaire = 0
#
vitesse=-4
#
proch_cac=30
# limite de catus proches
lim_cactus = 0
# chargement des images
import os
repActuel = os.getcwd()
pyxel.load(os.path.join(repActuel,"dessin_étoile_julie_emma.pyxres"))


def dino_deplacement():        
    # Pour pouvoir modifier ces variables, il faut d'abord les déclarer comme globales
    global dinoY, dinoVit, dinoX
    
    # Détection de la touche échap pour arrêter le  jeu
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()  
    # Si le dino est au sol et qu'on appuie sur ESPACE
    if dinoY==solY and (pyxel.btn(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)):
        # On donne une vitesse négative (vers le haut) au dino
        dinoVit=-15
              
def cactus_creation():
    """création aléatoire des ennemis"""
    global proch_cac, lim_cactus
    proch_cac-=1
    if proch_cac==0:
        cactus_liste.append([240, 80])
        if (random.random()>0.5) or (lim_cactus>=3):
           proch_cac=random.randint(25,35)
           lim_cactus = 1
        else:
            proch_cac=random.randint(3,8)
            lim_cactus += 1

def cactus_deplacement():
    for cactu in cactus_liste:
        cactu[0] += vitesse  
    for cactu in cactus_liste: 
        if  cactu[0]<-16:
            cactus_liste.remove(cactu)
               
def dino_suppression():
    global playing
    for cactu in cactus_liste:
        if cactu[0] <= dinoX+8 and cactu[1] <= dinoY+8 and cactu[0]+8 >= dinoX and cactu[1]+8 >= dinoY:
            playing=3

def update():
    dino_deplacement()
    #print(dinosaure_y)
        # Pour pouvoir modifier ces variables, il faut d'abord les déclarer comme globales
    global dinoY, dinoVit, dinoX, playing

    if playing==0:
          # Détection de la touche échap pour arrêter le  jeu
          if pyxel.btnp(pyxel.KEY_Q):
              pyxel.quit()
              
          # suppression du vaisseau et ennemi si contact
          dino_suppression()
              
          # creation des ennemis
          #cactus_liste = cactus_creation(cactus_liste)
          cactus_creation()
          cactus_deplacement()
              
          # Pour chaque frame, on déplace le dino de sa vitesse en Y
          dinoY = dinoY + dinoVit
          # Pour chaque frame, la vitesse est modifiée par la gravité
          dinoVit = dinoVit + dinoGravite
          # Si le dino est au niveau du sol ou plus bas
          if (dinoY>=solY):
              # On le place sur le sol s'il était plus bas 
              dinoY=solY
              # On annulle sa vitesse en Y
              dinoVit=0

def draw():
   global imagePaire, vitesse, playing, cactus_liste, frames
   frames = frames +1
   pyxel.cls(0)    
     
   if playing == 0:    
     pyxel.text(80,15, str(frames), 7)
     # Affichage du 'dino'
     #pyxel.rect(dinoX,dinoY,h=dinoTaille,w=dinoTaille,col=9)
     
     if not (pyxel.frame_count % 4):
         imagePaire=1-imagePaire
     pyxel.blt(dinoX, dinoY, 0, 152, 120+dinoTaille*imagePaire, 20, dinoTaille,0)
     
  #   for i in range (3):
 #        pyxel.blt(160+i*30, 5, 0, 152, 56, 20, 30)
     
#         if pyxel.frame_count>=500*(i+1)+500*(i):
#             pyxel.blt(160+i*30, 5, 0, 150, 90, 25, 30)

     etoile1=pyxel.blt(160, 5, 0, 152, 56, 20, 30)
     etoile2=pyxel.blt(190, 5, 0, 152, 56, 20, 30)
     etoile3=pyxel.blt(220, 5, 0, 152, 56, 20, 30)
     
     if frames>=500:
         etoile1=pyxel.blt(160, 5, 0, 150, 90, 25, 30)
         vitesse=-5
     if frames>=1500:
         etoile2=pyxel.blt(190, 5, 0, 150, 90, 25, 30)
         vitesse=-6
     if frames>=2500:
         etoile3=pyxel.blt(220, 5, 0, 150, 90, 25, 30)
         if dinoY==solY:
            playing=2
             
    
    # ennemis
     for cactu in cactus_liste:
        #pyxel.rect(cactu[0], cactu[1], 10, 20, 3)
        pyxel.blt(cactu[0], cactu[1], 0, 123, 116, 16, 35, 0)

     
        
     # sinon: GAME OVER
   else:
        for cactu in cactus_liste:
            pyxel.blt(cactu[0], cactu[1], 0, 123, 116, 16, 35, 0)
            
        if playing==1:
           pyxel.text(85,50, 'PRESS SPACE TO START', 7) 
           pyxel.blt(dinoX, dinoY, 0, 152, 120, 20, dinoTaille,0) 
           if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
               playing=0
           
           
        if playing==2:
              pyxel.text(100,50, 'VICTORY !', 7)
              pyxel.blt(60, 30, 0, 152, 24, 32, 20,0) 
              pyxel.blt(dinoX, dinoY, 0, 152, 120+dinoTaille*3, 20, dinoTaille,0) 
              if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
               playing=1
               cactus_liste = []
               vitesse=-4
               frames=0              
             
        if playing==3:    
          pyxel.text(100,50, 'GAME OVER', 7)
          pyxel.blt(60, 30, 0, 152, 0, 32, 20,0) 
          pyxel.blt(dinoX, dinoY, 0, 152, 120+dinoTaille*2, 20, dinoTaille,0)      
          if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
               playing=1
               cactus_liste = []
               vitesse=-4
               frames=0
          
pyxel.run(update, draw)

 