import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
pygame.display.set_caption('Meteor shooter')
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
# test_surface = pygame.Surface((400,100))

# importin images
ship_surf = pygame.image.load('../images/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

bg_surf = pygame.image.load('../images/background.png').convert()

# import text
font = pygame.font.Font('../font/subatomic.ttf', 50)
text_surf = font.render("Space", True, 'White')
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT - 80) )
while True:
	# 1. 입력
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	# framerate limitation
	clock.tick(120)

	# 2. 업데이트
	display_surface.fill((200,200,200))
	display_surface.blit(bg_surf,(0,0))


	if ship_rect.y > 0:
		ship_rect.y -= 4
	display_surface.blit(ship_surf,ship_rect)
	display_surface.blit(text_surf,text_rect)
	# test_surface.fill((186,120,39))
	# display_surface.blit(test_surface,(WINDOW_WIDTH-test_surface.get_width(),50))



	# 3. 프레임 보여주기
	pygame.display.update()
