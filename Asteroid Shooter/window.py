import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
pygame.display.set_caption('Meteor shooter')
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# test_surface = pygame.Surface((400,100))

# importin images
ship_surf = pygame.image.load('../images/ship.png').convert_alpha()
bg_surf = pygame.image.load('../images/background.png').convert()

# import text
font = pygame.font.Font('../font/subatomic.ttf', 50)
text_surf = font.render("Space", True, 'White')

while True:
	# 1. 입력
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			

			sys.exit()

	# 2. 업데이트
	display_surface.fill((200,200,200))
	display_surface.blit(bg_surf,(0,0))
	display_surface.blit(ship_surf,(300,500))
	display_surface.blit(text_surf,(500,240))
	# test_surface.fill((186,120,39))
	# display_surface.blit(test_surface,(WINDOW_WIDTH-test_surface.get_width(),50))



	# 3. 프레임 보여주기
	pygame.display.update()
