import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720


# 윈도우창 이름 바꾸기
pygame.display.set_caption('Meteor shooter')

# 창띄우기
dispay_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# keeps the code going
while True:
	# 1. 입력
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			

			sys.exit()

	# 2. 업데이트

	# 3. 프레임 보여주기
	pygame.display.update()
