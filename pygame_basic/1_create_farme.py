import pygame

pygame.init() # 초기화 작업 (필수)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# # 화면 타이틀 설정
# pygame.display.set_caption("Nado game") # 게임 이름

# 이벤트 루프가 있어야 창이 안꺼짐
# 이벤트 루프
running = True # 게임이 진행중인가 ?
while running:
    for event in pygame.event.get(): # 이벤트가 발생하였는가 ?
        if event.type == pygame.QUIT: # 만약 창이 닫히는 이벤트가 발생한다면
            running = False 

# pygame 종료
pygame.quit()