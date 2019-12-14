import pygame


def getoutput(r1,r2,dist):
	if dist==0:
		output='circles are concentric'
		return output
	else:
		if r1-r2>0:
			if dist>r1-r2 and dist<r1+r2:
				output='Circles have 2 points of intersection'
				return output
			if dist>r1-r2 and dist==r1+r2:
				output='Circles have 1 point of intersection'
				return output
			if dist>r1-r2 and dist>r1+r2:
				output='Circles have no point of intersection'
				return output

			if dist==r1-r2:
				output='Circles have 1 point of intersection'
				return output
			else:
				output='Circles have no point of intersection'
				return output
		else:
			if dist>r2-r1 and dist<r2+r1:
				output='Circles have 2 points of intersection'
				return output
			if dist>r2-r1 and dist==r2+r1:
				output='Circles have 1 point of intersection'
				return output
			if dist>r2-r1 and dist>r2+r1:
				output='Circles have no point of intersection'
				return output

			if dist==r2-r1:
				output='Circles have 1 point of intersection'
				return output
			else:
				output='Circles have no point of intersection'
				return output


r1=int(input('Enter Radius 1: '))
r2=int(input('Enter Radius 2: '))
dist=int(input('Enter Distance between the Circles: '))

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((1000,700))


pygame.draw.line(gameDisplay, blue, (300,0), (300,699),4)
font=pygame.font.SysFont('ubuntu',30)
text1 = font.render('Radius 1: '+str(r1), True, (229, 237, 78), black)
TextRect1 = text1.get_rect()
TextRect1.center=(120,60)
gameDisplay.blit(text1,TextRect1)

text2 = font.render('Radius 2: '+str(r2), True, (229, 237, 78), black)
TextRect2 = text1.get_rect()
TextRect2.center=(120,120)
gameDisplay.blit(text2,TextRect2)

text3 = font.render('Distance: '+str(dist), True, (229, 237, 78), black)
TextRect3 = text1.get_rect()
TextRect3.center=(120,180)
gameDisplay.blit(text3,TextRect3)

text4 = font.render('Output: ', True, white, black)
TextRect4 = text1.get_rect()
TextRect4.center=(700,60)
gameDisplay.blit(text4,TextRect4)

output=getoutput(r1,r2,dist)
text5 = font.render(output, True, white, black)
TextRect5 = text1.get_rect()
TextRect5.center=(450,120)
gameDisplay.blit(text5,TextRect5)


#Draw both the circles and radius
if r1>r2:
	pygame.draw.circle(gameDisplay, (255,255,150), (600,450), r1)
	pygame.draw.circle(gameDisplay, (255,180,150), (600,450+dist), r2)
	pygame.draw.line(gameDisplay, green,(600,450), (600+r1,450), 2)
	pygame.draw.line(gameDisplay, red,(600,450+dist), (600,450+r2+dist), 2)
else:
	pygame.draw.circle(gameDisplay, (255,180,150), (600,450+dist), r2)
	pygame.draw.circle(gameDisplay, (255,255,150), (600,450), r1)
	pygame.draw.line(gameDisplay, green,(600,450), (600+r1,450), 2)
	pygame.draw.line(gameDisplay, red,(600,450+dist), (600,450+r2+dist), 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        	pygame.display.quit()
        	pygame.quit()
        	quit()

    pygame.display.update()
